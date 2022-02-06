from django.test import TestCase

# Create your tests here.

# <form method="POST">
#     {% csrf_token %}
#     <label for="authors">Автор</label>
#     <select name="authors" size="4">
#
#     <label for="title">Название</label>
#     <input name="title" type="text">
#
#     <label for="text">Текст</label>
#     <input name="text" type="text">
#
#     <!-- Здесь будет список категорий.  -->
#     <label for="categories">Категория</label>
#     <select name="categories" size="4">
#
#       {% for category in categories %}
#         <option value="{{ category.id }}">
#             {{ category.name }}
#         </option>
#       {% endfor %}
#     </select>
#     <input type="submit" value="Добавить новость">
# </form>
