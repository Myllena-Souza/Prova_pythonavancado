from django.contrib import admin
from lojaTaygra_app.models import Produto
from lojaTaygra_app.models import Imagem
from lojaTaygra_app.models import Categoria
from lojaTaygra_app.models import SubCategoria
from lojaTaygra_app.models import Desconto
from lojaTaygra_app.models import Contato


admin.site.register(Produto)
admin.site.register(Imagem)
admin.site.register(Categoria)
admin.site.register(SubCategoria)
admin.site.register(Desconto)
admin.site.register(Contato)