import pytest
from django.urls import reverse
from core.models import Processamento
from core.tasks import save_resultado


@pytest.mark.django_db
class TestProcessamentoEndpoints:

    def test_criacao_valida(self, client):
        response = client.post(reverse("processamento-processar"), {
            "numero1": 5,
            "numero2": 15,
            "numero3": 25,
        }, content_type="application/json")
        assert response.status_code == 201

    def test_dados_invalidos(self, client):
        response = client.post(reverse("processamento-processar"), {}, content_type="application/json")
        assert response.status_code == 400
        assert "numero1" in response.json()

    def test_dados_parciais(self, client):
        response = client.post(reverse("processamento-processar"), {"numero1": 10}, content_type="application/json")
        json_data = response.json()
        assert response.status_code == 400
        assert "numero2" in json_data
        assert "numero3" in json_data

    def test_tipos_invalidos(self, client):
        response = client.post(reverse("processamento-processar"), {
            "numero1": "a", "numero2": "b", "numero3": "c"
        }, content_type="application/json")
        assert response.status_code == 400


    def test_listar_vazio(self, client):
        response = client.get(reverse("processamento-list"))
        assert response.status_code == 200
        assert response.json() == []

    def test_listar_nao_vazio(self, client):
        client.post(reverse("processamento-processar"), {
            "numero1": 1, "numero2": 2, "numero3": 3
        }, content_type="application/json")

        response = client.get(reverse("processamento-list"))
        assert response.status_code == 200
        assert len(response.json()) >= 1

    def test_recuperar_por_id(self, client):
        resp = client.post(reverse("processamento-processar"), {
            "numero1": 10, "numero2": 20, "numero3": 30
        }, content_type="application/json")
        p_id = resp.json()["id"]

        response = client.get(reverse("processamento-detail", args=[p_id]))
        assert response.status_code == 200
        assert response.json()["id"] == p_id

    def test_get_inexistente(self, client):
        response = client.get(reverse("processamento-detail", args=[9999]))
        assert response.status_code == 404

@pytest.mark.django_db
class TestProcessamentoTasks:

    def test_salva_media(self):
        p = Processamento.objects.create(numero1=10, numero2=20, numero3=30)
        save_resultado({'processamento_id': p.id, 'media': 20.0})
        p.refresh_from_db()
        assert p.media == 20.0

    def test_salva_mediana(self):
        p = Processamento.objects.create(numero1=3, numero2=1, numero3=2)
        save_resultado({'processamento_id': p.id, 'mediana': 2})
        p.refresh_from_db()
        assert p.mediana == 2

    def test_conclui_quando_ambos_presentes(self):
        p = Processamento.objects.create(numero1=4, numero2=5, numero3=6)
        save_resultado({'processamento_id': p.id, 'media': 5.0})
        save_resultado({'processamento_id': p.id, 'mediana': 5})
        p.refresh_from_db()
        assert p.status == "Concluído"

    def test_nao_conclui_com_dado_parcial(self):
        p = Processamento.objects.create(numero1=5, numero2=6, numero3=7)
        save_resultado({'processamento_id': p.id, 'media': 6.0})
        p.refresh_from_db()
        assert p.status == "Processando.."


@pytest.mark.django_db
def test_model_criacao():
    p = Processamento.objects.create(numero1=7, numero2=8, numero3=9)
    assert (p.numero1, p.numero2, p.numero3) == (7, 8, 9)
    assert p.status == "Processando.."
