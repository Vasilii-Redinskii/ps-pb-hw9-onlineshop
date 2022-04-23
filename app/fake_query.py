from app.models import Brand


brands_list = Brand.query.all()
for brand in brands_list:
    print(f'Товары бренда {brand.title}: {brand.items}')