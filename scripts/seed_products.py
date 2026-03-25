import asyncio
import httpx

def generate_products():
    products = []

    smartphones = [
        ("Apple iPhone 17 Pro", "Apple", 1099.00, "A19 Pro chip, 6.3 inch ProMotion OLED, 48MP triple camera, titanium frame, 5x optical zoom", {"Chip":"A19 Pro","Display":"6.3 inch ProMotion OLED 120Hz","Camera":"48MP triple, 5x zoom","Battery":"27hr","Connector":"USB-C"}, 4.9, 1243),
        ("Apple iPhone 17", "Apple", 899.00, "A19 chip, 6.1 inch OLED display, 48MP dual camera, aluminum frame, USB-C", {"Chip":"A19","Display":"6.1 inch OLED","Camera":"48MP dual","Battery":"24hr"}, 4.8, 3421),
        ("Apple iPhone 16 Pro Max", "Apple", 1199.00, "A18 Pro chip, 6.7 inch display, 48MP camera system, titanium", {"Chip":"A18 Pro","Display":"6.7 inch OLED","Camera":"48MP triple"}, 4.9, 8921),
        ("Apple iPhone 16 Pro", "Apple", 999.00, "A18 Pro chip, 6.3 inch display, 48MP triple camera, titanium design", {"Chip":"A18 Pro","Display":"6.3 inch OLED","Camera":"48MP triple"}, 4.8, 12043),
        ("Apple iPhone 16", "Apple", 799.00, "A18 chip, 6.1 inch OLED, 48MP dual camera, USB-C", {"Chip":"A18","Display":"6.1 inch OLED","Camera":"48MP dual"}, 4.7, 23412),
        ("Apple iPhone 15 Pro", "Apple", 899.00, "A17 Pro chip, titanium, USB-C 3, 48MP main camera", {"Chip":"A17 Pro","Display":"6.1 inch OLED","Camera":"48MP, 3x zoom"}, 4.9, 45231),
        ("Apple iPhone SE 3rd Gen", "Apple", 429.00, "A15 Bionic, 4.7 inch LCD, 12MP camera, Touch ID, 5G", {"Chip":"A15","Display":"4.7 inch LCD","Camera":"12MP"}, 4.4, 19823),
        ("Samsung Galaxy S25 Ultra", "Samsung", 1299.00, "Snapdragon 8 Elite, 6.9 inch QHD AMOLED, 200MP camera, S Pen included", {"Chip":"Snapdragon 8 Elite","Display":"6.9 inch QHD AMOLED","Camera":"200MP quad","RAM":"12GB"}, 4.8, 9871),
        ("Samsung Galaxy S25 Plus", "Samsung", 999.00, "Snapdragon 8 Elite, 6.7 inch AMOLED, 50MP triple camera", {"Chip":"Snapdragon 8 Elite","Display":"6.7 inch AMOLED","Camera":"50MP triple"}, 4.7, 7432),
        ("Samsung Galaxy S25", "Samsung", 799.00, "Snapdragon 8 Elite, 6.2 inch AMOLED 120Hz, 50MP triple camera", {"Chip":"Snapdragon 8 Elite","Display":"6.2 inch AMOLED","Camera":"50MP triple"}, 4.7, 15632),
        ("Samsung Galaxy S24 Ultra", "Samsung", 1099.00, "Snapdragon 8 Gen 3, 6.8 inch QHD AMOLED, 200MP camera, titanium, S Pen", {"Chip":"Snapdragon 8 Gen 3","Display":"6.8 inch QHD","Camera":"200MP quad"}, 4.8, 18234),
        ("Samsung Galaxy Z Fold 6", "Samsung", 1799.00, "Foldable 7.6 inch inner AMOLED, Snapdragon 8 Gen 3, 50MP triple camera", {"Chip":"Snapdragon 8 Gen 3","Inner Display":"7.6 inch AMOLED","Camera":"50MP triple"}, 4.6, 4231),
        ("Samsung Galaxy Z Flip 6", "Samsung", 999.00, "Flip foldable, 6.7 inch AMOLED, Snapdragon 8 Gen 3, 50MP dual camera", {"Chip":"Snapdragon 8 Gen 3","Display":"6.7 inch AMOLED","Camera":"50MP dual"}, 4.6, 5621),
        ("Samsung Galaxy A55", "Samsung", 449.00, "Exynos 1480, 6.6 inch Super AMOLED, 50MP triple camera, 5000mAh", {"Chip":"Exynos 1480","Display":"6.6 inch AMOLED","Camera":"50MP triple"}, 4.5, 18234),
        ("Samsung Galaxy A35", "Samsung", 349.00, "Exynos 1380, 6.6 inch Super AMOLED, 50MP triple camera", {"Chip":"Exynos 1380","Display":"6.6 inch AMOLED","Camera":"50MP triple"}, 4.4, 22134),
        ("Google Pixel 9 Pro XL", "Google", 1099.00, "Tensor G4, 6.8 inch LTPO OLED, 50MP triple camera, 7 years updates", {"Chip":"Tensor G4","Display":"6.8 inch OLED","Camera":"50MP triple","Updates":"7 years"}, 4.7, 6234),
        ("Google Pixel 9 Pro", "Google", 999.00, "Tensor G4, 6.3 inch OLED, 50MP triple camera, AI features", {"Chip":"Tensor G4","Display":"6.3 inch OLED","Camera":"50MP triple"}, 4.7, 8123),
        ("Google Pixel 9", "Google", 799.00, "Tensor G4, 6.3 inch OLED, 50MP dual camera, AI photo features", {"Chip":"Tensor G4","Display":"6.3 inch OLED","Camera":"50MP dual"}, 4.6, 11234),
        ("Google Pixel 8a", "Google", 499.00, "Tensor G3, 6.1 inch OLED 120Hz, 64MP dual camera, 7 years updates", {"Chip":"Tensor G3","Display":"6.1 inch OLED","Camera":"64MP dual"}, 4.6, 12341),
        ("OnePlus 13", "OnePlus", 899.00, "Snapdragon 8 Elite, 6.82 inch LTPO AMOLED, 50MP Hasselblad triple, 100W charging", {"Chip":"Snapdragon 8 Elite","Display":"6.82 inch AMOLED","Camera":"50MP Hasselblad","Charging":"100W"}, 4.6, 7821),
        ("OnePlus 12", "OnePlus", 799.00, "Snapdragon 8 Gen 3, 6.82 inch LTPO AMOLED, 50MP Hasselblad, 80W charging", {"Chip":"Snapdragon 8 Gen 3","Display":"6.82 inch AMOLED","Camera":"50MP Hasselblad"}, 4.5, 9234),
        ("Xiaomi 15 Pro", "Xiaomi", 999.00, "Snapdragon 8 Elite, 6.73 inch LTPO AMOLED, Leica 50MP triple camera, 90W charging", {"Chip":"Snapdragon 8 Elite","Display":"6.73 inch AMOLED","Camera":"50MP Leica triple"}, 4.6, 5432),
        ("Xiaomi 14 Ultra", "Xiaomi", 1299.00, "Snapdragon 8 Gen 3, 1-inch 50MP Leica quad camera, 90W charging", {"Chip":"Snapdragon 8 Gen 3","Camera":"1-inch 50MP Leica quad","Charging":"90W"}, 4.7, 3214),
        ("Nothing Phone 3", "Nothing", 799.00, "Snapdragon 8 Gen 3, 6.67 inch LTPO OLED, 50MP triple camera, Glyph Interface", {"Chip":"Snapdragon 8 Gen 3","Display":"6.67 inch OLED","Camera":"50MP triple"}, 4.5, 6234),
        ("Nothing Phone 2a", "Nothing", 399.00, "Dimensity 7200 Pro, 6.7 inch AMOLED 120Hz, 50MP dual camera", {"Chip":"Dimensity 7200 Pro","Display":"6.7 inch AMOLED","Camera":"50MP dual"}, 4.4, 8921),
        ("Motorola Edge 50 Pro", "Motorola", 599.00, "Snapdragon 7 Gen 3, 6.7 inch pOLED 144Hz, 50MP triple, 125W charging", {"Chip":"Snapdragon 7 Gen 3","Display":"6.7 inch pOLED 144Hz","Charging":"125W"}, 4.4, 6234),
        ("Motorola Moto G85", "Motorola", 299.00, "Snapdragon 6s Gen 3, 6.67 inch pOLED 120Hz, 50MP dual camera", {"Chip":"Snapdragon 6s Gen 3","Display":"6.67 inch pOLED","Camera":"50MP dual"}, 4.3, 9234),
        ("Sony Xperia 1 VI", "Sony", 1299.00, "Snapdragon 8 Gen 3, 6.5 inch 4K OLED 120Hz, Zeiss 52MP triple, 3.5mm jack", {"Chip":"Snapdragon 8 Gen 3","Display":"6.5 inch 4K OLED","Camera":"52MP Zeiss triple"}, 4.5, 2134),
        ("Realme GT 6", "Realme", 599.00, "Snapdragon 8s Gen 3, 6.78 inch AMOLED 120Hz, 50MP triple camera", {"Chip":"Snapdragon 8s Gen 3","Display":"6.78 inch AMOLED","Camera":"50MP triple"}, 4.4, 7823),
        ("Poco X6 Pro", "Poco", 399.00, "Dimensity 8300 Ultra, 6.67 inch AMOLED 120Hz, 64MP triple camera", {"Chip":"Dimensity 8300 Ultra","Display":"6.67 inch AMOLED","Camera":"64MP triple"}, 4.4, 9234),
    ]
    for i, (name, brand, price, desc, specs, rating, reviews) in enumerate(smartphones):
        products.append({"id": f"phone_{i+1:03d}", "name": name, "brand": brand, "category": "smartphones", "price": price, "description": desc, "specs": specs, "tags": ["smartphone", "mobile", brand.lower(), "5g"], "rating": rating, "review_count": reviews, "in_stock": True})

    laptops = [
        ("MacBook Pro 16 M4 Max", "Apple", 3499.00, "M4 Max chip, 16 inch Liquid Retina XDR, 36GB RAM, 1TB SSD, 22hr battery", {"Chip":"M4 Max","Display":"16 inch Liquid Retina XDR","RAM":"36GB","Storage":"1TB SSD","Battery":"22hr"}, 4.9, 3421),
        ("MacBook Pro 14 M4 Pro", "Apple", 1999.00, "M4 Pro chip, 14 inch Liquid Retina XDR, 24GB RAM, 512GB SSD, 18hr battery", {"Chip":"M4 Pro","Display":"14 inch Liquid Retina XDR","RAM":"24GB","Storage":"512GB SSD"}, 4.9, 5621),
        ("MacBook Air 15 M3", "Apple", 1299.00, "M3 chip, 15 inch Liquid Retina, 8GB RAM, 256GB SSD, 18hr battery, fanless", {"Chip":"M3","Display":"15 inch Liquid Retina","RAM":"8GB","Storage":"256GB SSD"}, 4.8, 12341),
        ("MacBook Air 13 M3", "Apple", 1099.00, "M3 chip, 13 inch Liquid Retina, 8GB RAM, 256GB SSD, 18hr battery", {"Chip":"M3","Display":"13 inch Liquid Retina","RAM":"8GB","Storage":"256GB SSD"}, 4.8, 18234),
        ("MacBook Air 13 M2", "Apple", 899.00, "M2 chip, 13 inch Liquid Retina, 8GB RAM, 256GB SSD, 18hr battery", {"Chip":"M2","Display":"13 inch Liquid Retina","RAM":"8GB","Storage":"256GB SSD"}, 4.8, 34521),
        ("Dell XPS 15 9530", "Dell", 1799.00, "Intel Core i9-13900H, 15.6 inch OLED 3.5K, 32GB RAM, 1TB SSD, RTX 4070", {"CPU":"Intel Core i9-13900H","Display":"15.6 inch OLED 3.5K","RAM":"32GB DDR5","GPU":"RTX 4070"}, 4.7, 6234),
        ("Dell XPS 13 9340", "Dell", 1299.00, "Intel Core Ultra 7, 13.4 inch FHD OLED, 16GB RAM, 512GB SSD", {"CPU":"Intel Core Ultra 7","Display":"13.4 inch OLED","RAM":"16GB","Storage":"512GB SSD"}, 4.6, 8923),
        ("Dell Inspiron 15 3000", "Dell", 549.00, "Intel Core i5-1335U, 15.6 inch FHD, 8GB RAM, 512GB SSD, Windows 11", {"CPU":"Intel Core i5","Display":"15.6 inch FHD","RAM":"8GB","Storage":"512GB"}, 4.3, 23412),
        ("ASUS ROG Strix G16 2024", "ASUS", 1799.00, "Intel Core i9-14900HX, 16 inch QHD 240Hz, 32GB RAM, 1TB SSD, RTX 4080", {"CPU":"Intel Core i9-14900HX","Display":"16 inch QHD 240Hz","RAM":"32GB DDR5","GPU":"RTX 4080"}, 4.8, 4521),
        ("ASUS ROG Strix G15", "ASUS", 1149.99, "AMD Ryzen 9 6900HX, 15.6 inch FHD 300Hz, 16GB RAM, 1TB SSD, RTX 3070 Ti", {"CPU":"AMD Ryzen 9 6900HX","Display":"15.6 inch FHD 300Hz","RAM":"16GB","GPU":"RTX 3070 Ti"}, 4.7, 2341),
        ("ASUS ZenBook 14 OLED", "ASUS", 999.00, "Intel Core Ultra 7, 14 inch 2.8K OLED, 16GB RAM, 512GB SSD, 89Whr battery", {"CPU":"Intel Core Ultra 7","Display":"14 inch 2.8K OLED","RAM":"16GB","Battery":"89Whr"}, 4.7, 8923),
        ("Lenovo ThinkPad X1 Carbon Gen 12", "Lenovo", 1799.00, "Intel Core Ultra 7, 14 inch 2.8K OLED, 32GB RAM, 1TB SSD, business ultrabook", {"CPU":"Intel Core Ultra 7","Display":"14 inch 2.8K OLED","RAM":"32GB","Weight":"1.12kg"}, 4.7, 5234),
        ("Lenovo ThinkPad T14s Gen 5", "Lenovo", 1299.00, "AMD Ryzen 7 PRO 8840U, 14 inch 2.8K OLED, 32GB RAM, 512GB SSD", {"CPU":"AMD Ryzen 7 PRO","Display":"14 inch 2.8K OLED","RAM":"32GB"}, 4.6, 6234),
        ("Lenovo IdeaPad Flex 5", "Lenovo", 649.00, "AMD Ryzen 5 7530U, 14 inch FHD touch 2-in-1, 8GB RAM, 512GB SSD", {"CPU":"AMD Ryzen 5","Display":"14 inch FHD touch","Type":"2-in-1"}, 4.4, 18234),
        ("HP Spectre x360 14", "HP", 1599.00, "Intel Core Ultra 7, 14 inch 2.8K OLED 120Hz touch 2-in-1, 32GB RAM, 1TB SSD", {"CPU":"Intel Core Ultra 7","Display":"14 inch 2.8K OLED 120Hz","Type":"2-in-1 convertible"}, 4.7, 7234),
        ("HP Envy x360 15", "HP", 999.00, "AMD Ryzen 7 8700U, 15.6 inch FHD OLED 120Hz 2-in-1, 16GB RAM, 512GB SSD", {"CPU":"AMD Ryzen 7","Display":"15.6 inch OLED 120Hz","Type":"2-in-1"}, 4.5, 9234),
        ("HP Pavilion 15", "HP", 649.00, "Intel Core i5-1335U, 15.6 inch FHD IPS, 8GB RAM, 512GB SSD, Windows 11", {"CPU":"Intel Core i5","Display":"15.6 inch FHD","RAM":"8GB"}, 4.3, 19234),
        ("Microsoft Surface Pro 11", "Microsoft", 1499.00, "Snapdragon X Elite, 13 inch 2K touchscreen, 16GB RAM, 512GB SSD, detachable", {"Chip":"Snapdragon X Elite","Display":"13 inch 2K 120Hz","Type":"Detachable tablet"}, 4.6, 4521),
        ("Microsoft Surface Laptop 6", "Microsoft", 1299.00, "Intel Core Ultra 5, 13.5 inch 2K touchscreen, 16GB RAM, 512GB SSD", {"CPU":"Intel Core Ultra 5","Display":"13.5 inch 2K","RAM":"16GB"}, 4.6, 5621),
        ("Razer Blade 15 2024", "Razer", 2499.00, "Intel Core i9-14900HX, 15.6 inch QHD 240Hz OLED, 32GB RAM, 1TB, RTX 4080", {"CPU":"Intel Core i9-14900HX","Display":"15.6 inch QHD OLED 240Hz","GPU":"RTX 4080"}, 4.7, 3421),
        ("Razer Blade 14", "Razer", 2499.00, "AMD Ryzen 9, 14 inch QHD 165Hz OLED, 32GB RAM, 1TB SSD, RTX 4070", {"CPU":"AMD Ryzen 9","Display":"14 inch QHD OLED 165Hz","GPU":"RTX 4070"}, 4.7, 3421),
        ("Acer Predator Helios 18", "Acer", 2499.00, "Intel Core i9-14900HX, 18 inch QHD 250Hz, 32GB RAM, 2TB SSD, RTX 4090", {"CPU":"Intel Core i9-14900HX","Display":"18 inch QHD 250Hz","GPU":"RTX 4090"}, 4.7, 2341),
        ("Acer Swift Go 14", "Acer", 799.00, "Intel Core Ultra 5, 14 inch 2.8K OLED, 16GB RAM, 512GB SSD, lightweight", {"CPU":"Intel Core Ultra 5","Display":"14 inch 2.8K OLED","Weight":"1.35kg"}, 4.5, 8234),
        ("LG Gram 17", "LG", 1699.00, "Intel Core Ultra 7, 17 inch WQXGA IPS, 32GB RAM, 1TB SSD, MIL-STD certified 1.35kg", {"CPU":"Intel Core Ultra 7","Display":"17 inch WQXGA","Weight":"1.35kg","Certification":"MIL-STD-810H"}, 4.7, 4234),
        ("LG Gram 14", "LG", 1299.00, "Intel Core Ultra 5, 14 inch WUXGA IPS, 16GB RAM, 512GB SSD, 1.04kg ultralight", {"CPU":"Intel Core Ultra 5","Display":"14 inch WUXGA","Weight":"1.04kg"}, 4.6, 6234),
        ("Samsung Galaxy Book4 Ultra", "Samsung", 2499.00, "Intel Core Ultra 9, 16 inch 3K AMOLED 120Hz, 32GB RAM, 1TB SSD, RTX 4070", {"CPU":"Intel Core Ultra 9","Display":"16 inch 3K AMOLED","GPU":"RTX 4070"}, 4.7, 3421),
        ("MSI Stealth 16 AI Studio", "MSI", 2999.00, "Intel Core Ultra 9, 16 inch UHD+ OLED 120Hz, 64GB RAM, 2TB SSD, RTX 4090", {"CPU":"Intel Core Ultra 9","Display":"16 inch UHD OLED","GPU":"RTX 4090","RAM":"64GB"}, 4.8, 2134),
        ("Gigabyte AORUS 17X", "Gigabyte", 2299.00, "Intel Core i9-14900HX, 17.3 inch QHD 240Hz, 32GB DDR5, 2TB SSD, RTX 4080", {"CPU":"Intel Core i9-14900HX","Display":"17.3 inch QHD 240Hz","GPU":"RTX 4080"}, 4.6, 1823),
        ("Framework Laptop 16", "Framework", 1399.00, "AMD Ryzen 7 7745HX, 16 inch 2560x1600 165Hz, 32GB RAM, 1TB SSD, modular design", {"CPU":"AMD Ryzen 7 7745HX","Display":"16 inch 2560x1600 165Hz","Feature":"Modular, repairable"}, 4.6, 4521),
        ("Toshiba Portege X30L", "Toshiba", 1499.00, "Intel Core Ultra 7, 13.3 inch FHD IPS, 16GB RAM, 512GB SSD, 875g ultralight", {"CPU":"Intel Core Ultra 7","Display":"13.3 inch FHD","Weight":"875g"}, 4.5, 2341),
    ]
    for i, (name, brand, price, desc, specs, rating, reviews) in enumerate(laptops):
        products.append({"id": f"laptop_{i+1:03d}", "name": name, "brand": brand, "category": "laptops", "price": price, "description": desc, "specs": specs, "tags": ["laptop", brand.lower(), "windows" if brand != "Apple" else "macos"], "rating": rating, "review_count": reviews, "in_stock": True})

    headphones = [
        ("Sony WH-1000XM5", "Sony", 349.99, "Industry-leading ANC headphones, 30hr battery, 8 microphones, Bluetooth 5.2, multipoint", {"ANC":"Industry-leading","Battery":"30hr","Microphones":"8","Bluetooth":"5.2","Weight":"250g"}, 4.8, 18562),
        ("Sony WH-1000XM4", "Sony", 279.99, "ANC headphones, 30hr battery, LDAC Hi-Res, multipoint connection, foldable", {"ANC":"Yes","Battery":"30hr","Codec":"LDAC","Bluetooth":"5.0"}, 4.7, 45231),
        ("Sony WF-1000XM5", "Sony", 299.99, "True wireless earbuds, best-in-class ANC, 24hr total, LDAC Hi-Res audio", {"ANC":"Yes","Battery":"8hr+16hr case","Codec":"LDAC"}, 4.7, 12341),
        ("Sony WF-1000XM4", "Sony", 199.99, "True wireless earbuds, ANC, 36hr total, LDAC, IPX4, wireless charging", {"ANC":"Yes","Battery":"8hr+28hr case","Water":"IPX4","Codec":"LDAC"}, 4.6, 23412),
        ("Bose QuietComfort Ultra Headphones", "Bose", 429.00, "Immersive audio, CustomTune ANC, 24hr battery, spatial audio, USB-C", {"ANC":"CustomTune","Battery":"24hr","Audio":"Spatial","Charging":"USB-C"}, 4.8, 8921),
        ("Bose QuietComfort 45", "Bose", 329.00, "ANC headphones, 24hr battery, Aware mode, lightweight comfortable design", {"ANC":"Yes","Battery":"24hr","Modes":"Quiet/Aware","Weight":"238g"}, 4.7, 23412),
        ("Bose QuietComfort Ultra Earbuds", "Bose", 299.00, "Best ANC earbuds, CustomTune technology, 6hr+18hr, IPX4 water resistant", {"ANC":"CustomTune","Battery":"6hr+18hr","Water":"IPX4"}, 4.7, 15234),
        ("Apple AirPods Pro 2nd Gen", "Apple", 249.00, "H2 chip, ANC, Transparency mode, Adaptive Audio, 30hr total, USB-C case", {"Chip":"H2","ANC":"Yes","Battery":"6hr+24hr","Water":"IPX4"}, 4.8, 67234),
        ("Apple AirPods 4 with ANC", "Apple", 179.00, "H2 chip, Active Noise Cancellation, USB-C, personalized spatial audio", {"Chip":"H2","ANC":"Yes","Battery":"5hr+30hr","Connector":"USB-C"}, 4.7, 34521),
        ("Apple AirPods 4", "Apple", 129.00, "H2 chip, USB-C, personalized spatial audio, 30hr total battery", {"Chip":"H2","Battery":"5hr+30hr","Connector":"USB-C"}, 4.6, 45231),
        ("Apple AirPods Max USB-C", "Apple", 549.00, "Over-ear headphones, H1 chip, ANC, Transparency, spatial audio, 20hr", {"Chip":"H1 x2","ANC":"Yes","Battery":"20hr","Connector":"USB-C"}, 4.7, 12341),
        ("Samsung Galaxy Buds3 Pro", "Samsung", 249.00, "ANC earbuds, 360 Audio, 6hr+30hr, IPX7 waterproof, blade design", {"ANC":"Yes","Battery":"6hr+30hr","Water":"IPX7"}, 4.6, 8923),
        ("Sennheiser Momentum 4 Wireless", "Sennheiser", 349.00, "ANC headphones, 60hr battery, LDAC, adaptive ANC, foldable design", {"ANC":"Yes","Battery":"60hr","Codec":"LDAC"}, 4.7, 7234),
        ("Sennheiser IE 600", "Sennheiser", 699.00, "In-ear monitor, 7mm TrueResponse driver, amorphous zirconium housing, audiophile", {"Driver":"7mm TrueResponse","Housing":"Amorphous zirconium","Impedance":"18 ohm"}, 4.8, 2134),
        ("Jabra Evolve2 85", "Jabra", 449.00, "Professional ANC headphones, 8-mic array, 37hr battery, UC certified for Teams", {"ANC":"Yes","Battery":"37hr","Microphones":"8","Certification":"Microsoft Teams"}, 4.7, 5234),
        ("JBL Live 770NC", "JBL", 149.99, "ANC headphones, 65hr battery, Smart Ambient, hands-free Google Assistant", {"ANC":"Yes","Battery":"65hr","Assistant":"Google/Alexa"}, 4.5, 12341),
        ("Anker Soundcore Q45", "Anker", 79.99, "Budget ANC headphones, 50hr battery, multipoint connection, foldable", {"ANC":"Yes","Battery":"50hr","Multipoint":"Yes"}, 4.4, 45231),
        ("Audio-Technica ATH-M50xBT2", "Audio-Technica", 199.00, "Wireless studio headphones, 50hr battery, multipoint, hi-res audio", {"Battery":"50hr","Codec":"LDAC, AAC","Driver":"45mm"}, 4.7, 18234),
        ("Jabra Evolve2 55", "Jabra", 349.00, "Professional wireless headset, ANC, 50hr battery, FlexBoom mic, UC certified", {"ANC":"Yes","Battery":"50hr","Mic":"FlexBoom","Certification":"UC/Teams"}, 4.6, 6234),
        ("Beyerdynamic DT 900 Pro X", "Beyerdynamic", 299.00, "Open-back studio headphones, 48 ohm, STELLAR.45 driver, mixing and mastering", {"Type":"Open-back","Impedance":"48 ohm","Driver":"STELLAR.45","Use":"Studio mixing"}, 4.8, 3421),
        ("Shure Aonic 50 Gen 2", "Shure", 299.00, "ANC headphones, 45hr battery, LDAC, USB-C, app-controlled EQ", {"ANC":"Yes","Battery":"45hr","Codec":"LDAC","EQ":"App controlled"}, 4.7, 5234),
        ("Marshall Monitor III ANC", "Marshall", 249.99, "ANC headphones, 80hr battery, Bluetooth 5.3, classic Marshall rock design", {"ANC":"Yes","Battery":"80hr","Bluetooth":"5.3","Design":"Classic Marshall"}, 4.6, 7234),
        ("Skullcandy Crusher ANC 2", "Skullcandy", 199.99, "ANC headphones with haptic bass, 50hr battery, personal sound, Tile tracking", {"ANC":"Yes","Battery":"50hr","Bass":"Haptic","Tracking":"Tile built-in"}, 4.5, 9234),
        ("Razer Barracuda X 2022", "Razer", 99.99, "Wireless gaming headset, 2.4GHz + Bluetooth, 50hr battery, USB-C dongle", {"Battery":"50hr","Wireless":"2.4GHz + BT","Mic":"Detachable","Charging":"USB-C"}, 4.5, 12341),
        ("HyperX Cloud III Wireless", "HyperX", 149.99, "Gaming wireless headset, 120hr battery, 2.4GHz, DTS Headphone:X spatial", {"Battery":"120hr","Wireless":"2.4GHz","Audio":"DTS Headphone:X","Driver":"53mm"}, 4.7, 8923),
        ("Logitech G535 Lightspeed", "Logitech", 149.99, "Wireless gaming headset, 33hr battery, 40mm drivers, lightweight 236g", {"Battery":"33hr","Wireless":"LIGHTSPEED","Driver":"40mm","Weight":"236g"}, 4.5, 6234),
        ("SteelSeries Arctis Nova Pro", "SteelSeries", 349.99, "Multi-system wireless headset, ANC, hot-swap battery, Hi-Res certified", {"ANC":"Yes","Battery":"Hot-swap infinite","HiRes":"Yes","Compatibility":"PC/PS/Xbox"}, 4.7, 9234),
        ("Astro A50 Gen 5", "Astro", 299.99, "Wireless gaming headset, Dolby Audio, 24hr battery, base station, PS/PC", {"Battery":"24hr","Base Station":"Yes","Audio":"Dolby","Compatibility":"PS/PC"}, 4.6, 7234),
        ("Corsair HS80 RGB Wireless", "Corsair", 129.99, "Wireless gaming headset, Dolby Atmos, 20hr battery, Slipstream, RGB", {"Battery":"20hr","Wireless":"Slipstream 2.4GHz","Audio":"Dolby Atmos"}, 4.5, 8923),
        ("Turtle Beach Stealth Pro", "Turtle Beach", 269.99, "Multi-platform wireless headset, ANC, swappable batteries, 80hr total", {"ANC":"Yes","Battery":"Swappable 80hr total","Compatibility":"PS/Xbox/PC/Switch"}, 4.6, 5234),
    ]
    for i, (name, brand, price, desc, specs, rating, reviews) in enumerate(headphones):
        products.append({"id": f"audio_{i+1:03d}", "name": name, "brand": brand, "category": "audio", "price": price, "description": desc, "specs": specs, "tags": ["headphones", "audio", brand.lower(), "wireless"], "rating": rating, "review_count": reviews, "in_stock": True})

    tvs = [
        ("LG C4 OLED 77 inch", "LG", 2499.99, "OLED evo panel, 77 inch, alpha 9 AI Processor Gen7, Dolby Vision, 4 HDMI 2.1 ports, 144Hz gaming", {"Panel":"OLED evo","Size":"77 inch","Refresh":"144Hz","HDMI":"4x HDMI 2.1","HDR":"Dolby Vision"}, 4.9, 8921),
        ("LG C4 OLED 65 inch", "LG", 1596.99, "OLED evo panel, 65 inch, alpha 9 AI Gen7, Dolby Vision, 4 HDMI 2.1, 144Hz", {"Panel":"OLED evo","Size":"65 inch","Refresh":"144Hz","HDMI":"4x HDMI 2.1"}, 4.9, 12341),
        ("LG C4 OLED 55 inch", "LG", 1196.99, "OLED evo panel, 55 inch, alpha 9 AI Gen7, 4 HDMI 2.1 ports, 144Hz gaming", {"Panel":"OLED evo","Size":"55 inch","Refresh":"144Hz","HDMI":"4x HDMI 2.1"}, 4.9, 15234),
        ("LG C3 OLED 65 inch", "LG", 1496.99, "OLED evo panel, 65 inch, alpha 9 AI Gen6, Dolby Vision, 4 HDMI 2.1, 120Hz", {"Panel":"OLED evo","Size":"65 inch","Refresh":"120Hz","HDMI":"4x HDMI 2.1"}, 4.9, 18234),
        ("LG C3 OLED 55 inch", "LG", 1296.99, "OLED evo panel, 55 inch, alpha 9 AI Gen6, Dolby Vision IQ, 4 HDMI 2.1", {"Panel":"OLED evo","Size":"55 inch","Refresh":"120Hz","HDMI":"4x HDMI 2.1"}, 4.9, 12054),
        ("LG G4 OLED 65 inch", "LG", 2196.99, "Brightest LG OLED, Gallery series, 65 inch, 3000 nit, Dolby Vision, 144Hz", {"Panel":"OLED evo Gallery","Size":"65 inch","Brightness":"3000 nit","Refresh":"144Hz"}, 4.9, 5234),
        ("Samsung QN90D Neo QLED 65 inch", "Samsung", 1999.99, "Neo QLED 4K, 65 inch, Quantum HDR 2000, 144Hz, 4 HDMI 2.1, Anti-Glare", {"Panel":"Neo QLED","Size":"65 inch","HDR":"Quantum HDR 2000","Refresh":"144Hz"}, 4.8, 6234),
        ("Samsung QN85D Neo QLED 75 inch", "Samsung", 2299.99, "Neo QLED 4K, 75 inch, Quantum HDR 1500, 120Hz, 4 HDMI 2.1 ports", {"Panel":"Neo QLED","Size":"75 inch","HDR":"Quantum HDR 1500","Refresh":"120Hz"}, 4.7, 4521),
        ("Samsung S95D QD-OLED 65 inch", "Samsung", 2499.99, "QD-OLED 4K, 65 inch, Quantum HDR OLED, 144Hz, 4 HDMI 2.1, One Connect Box", {"Panel":"QD-OLED","Size":"65 inch","Refresh":"144Hz","Feature":"One Connect Box"}, 4.9, 4234),
        ("Sony A95L QD-OLED 65 inch", "Sony", 2999.99, "QD-OLED panel, 65 inch, XR Cognitive Processor, Dolby Vision, 4 HDMI 2.1", {"Panel":"QD-OLED","Size":"65 inch","Processor":"XR Cognitive","HDR":"Dolby Vision"}, 4.9, 3421),
        ("Sony A80L OLED 55 inch", "Sony", 1799.99, "OLED 4K, 55 inch, XR Processor, Dolby Vision, Acoustic Surface Audio, HDMI 2.1", {"Panel":"OLED","Size":"55 inch","Audio":"Acoustic Surface","Refresh":"120Hz"}, 4.8, 5234),
        ("Sony X90L LED 65 inch", "Sony", 1299.99, "Full Array LED 4K, 65 inch, XR Processor, Dolby Vision, HDMI 2.1, 120Hz", {"Panel":"Full Array LED","Size":"65 inch","Refresh":"120Hz","HDR":"Dolby Vision"}, 4.7, 7234),
        ("TCL QM8 Mini-LED 65 inch", "TCL", 999.99, "Mini-LED QLED 4K, 65 inch, 240Hz, Dolby Vision IQ, 4 HDMI 2.1, Google TV", {"Panel":"Mini-LED QLED","Size":"65 inch","Refresh":"240Hz","OS":"Google TV"}, 4.7, 8923),
        ("TCL QM8 Mini-LED 75 inch", "TCL", 1299.99, "Mini-LED QLED 4K, 75 inch, 240Hz, Dolby Vision, 4 HDMI 2.1, Google TV", {"Panel":"Mini-LED QLED","Size":"75 inch","Refresh":"240Hz","OS":"Google TV"}, 4.7, 6234),
        ("Hisense U8K Mini-LED 65 inch", "Hisense", 899.99, "Mini-LED ULED 4K, 65 inch, 144Hz, Dolby Vision IQ, 4 HDMI 2.1, Google TV", {"Panel":"Mini-LED ULED","Size":"65 inch","Refresh":"144Hz","OS":"Google TV"}, 4.6, 9234),
        ("Hisense U7K 55 inch", "Hisense", 599.99, "ULED 4K, 55 inch, 60W speakers, Dolby Vision, Google TV, HDMI 2.1", {"Panel":"ULED","Size":"55 inch","Audio":"60W","OS":"Google TV"}, 4.5, 12341),
        ("Vizio P-Series Quantum 65 inch", "Vizio", 799.99, "Quantum Color 4K, 65 inch, ProGaming Engine, 120Hz, HDMI 2.1, Dolby Vision", {"Panel":"Quantum Color","Size":"65 inch","Refresh":"120Hz","Gaming":"ProGaming Engine"}, 4.5, 7234),
        ("Amazon Fire TV Omni QLED 65 inch", "Amazon", 799.99, "QLED 4K, 65 inch, Fire TV built-in, Alexa, ambient display, HDR10+", {"Panel":"QLED","Size":"65 inch","OS":"Fire TV","Assistant":"Alexa"}, 4.4, 8923),
        ("Philips OLED 808 55 inch", "Philips", 1499.99, "OLED 4K, 55 inch, Ambilight 4-sided, P5 AI Processor, Dolby Vision, 120Hz", {"Panel":"OLED","Size":"55 inch","Feature":"Ambilight 4-sided","Refresh":"120Hz"}, 4.7, 3421),
        ("Panasonic Z95A OLED 65 inch", "Panasonic", 2299.99, "Master OLED Pro, 65 inch, HCX Pro AI Mk II processor, Dolby Vision IQ, 144Hz", {"Panel":"Master OLED Pro","Size":"65 inch","Refresh":"144Hz","HDR":"Dolby Vision IQ"}, 4.8, 2134),
    ]
    for i, (name, brand, price, desc, specs, rating, reviews) in enumerate(tvs):
        products.append({"id": f"tv_{i+1:03d}", "name": name, "brand": brand, "category": "televisions", "price": price, "description": desc, "specs": specs, "tags": ["tv", "television", "4k", "smart tv", brand.lower()], "rating": rating, "review_count": reviews, "in_stock": True})

    gaming_products = [
        ("PlayStation 5 Pro", "Sony", 699.99, "PS5 Pro with enhanced GPU, 2TB SSD, 4K 60fps ray tracing, 8K support, Wi-Fi 7", {"GPU":"Enhanced RDNA","Storage":"2TB SSD","Resolution":"4K/8K","WiFi":"Wi-Fi 7"}, 4.9, 34521),
        ("PlayStation 5 Slim Disc", "Sony", 449.99, "PS5 Slim with disc drive, 1TB SSD, smaller lighter form factor", {"Storage":"1TB SSD","Disc":"Yes","Size":"Slim"}, 4.8, 45231),
        ("PlayStation 5 Slim Digital", "Sony", 399.99, "PS5 Slim digital edition, 1TB SSD, no disc drive, compact design", {"Storage":"1TB SSD","Disc":"No","Size":"Slim"}, 4.7, 38234),
        ("Xbox Series X", "Microsoft", 499.99, "4K gaming, 1TB SSD, 120fps, Quick Resume, Game Pass, Wi-Fi 6E, 12 teraflops", {"Storage":"1TB NVMe SSD","Resolution":"4K 120fps","WiFi":"Wi-Fi 6E","Power":"12 teraflops"}, 4.8, 42341),
        ("Xbox Series S Carbon Black", "Microsoft", 299.99, "1440p gaming, 1TB SSD, 120fps, all-digital, compact carbon black", {"Storage":"1TB SSD","Resolution":"1440p 120fps","Color":"Carbon Black"}, 4.6, 28921),
        ("Nintendo Switch 2", "Nintendo", 449.99, "4K docked gaming, 1080p handheld, 7.9 inch LCD, improved Joy-Con, new C button", {"Display":"7.9 inch LCD","Docked":"4K","Handheld":"1080p"}, 4.9, 28734),
        ("Nintendo Switch OLED", "Nintendo", 349.99, "7 inch OLED screen, 64GB storage, enhanced audio, wide adjustable stand", {"Display":"7 inch OLED","Storage":"64GB"}, 4.8, 67234),
        ("Nintendo Switch Lite", "Nintendo", 199.99, "Compact handheld only, 5.5 inch LCD, 32GB, all colors, lightweight 275g", {"Display":"5.5 inch LCD","Storage":"32GB","Weight":"275g","Mode":"Handheld only"}, 4.7, 89234),
        ("Steam Deck OLED 1TB", "Valve", 649.00, "AMD APU, 7.4 inch OLED HDR 90Hz, 1TB NVMe, 50Whr battery, handheld PC gaming", {"Display":"7.4 inch OLED HDR","Storage":"1TB NVMe","Battery":"50Whr"}, 4.8, 23412),
        ("Steam Deck OLED 512GB", "Valve", 549.00, "AMD APU, 7.4 inch OLED HDR, 512GB NVMe, handheld PC gaming, SteamOS", {"Display":"7.4 inch OLED HDR","Storage":"512GB NVMe"}, 4.8, 18234),
        ("ASUS ROG Ally X", "ASUS", 899.99, "AMD Ryzen Z1 Extreme, 7 inch FHD 120Hz, 24GB RAM, 1TB SSD, Windows 11 gaming", {"CPU":"AMD Ryzen Z1 Extreme","Display":"7 inch FHD 120Hz","RAM":"24GB"}, 4.6, 8923),
        ("Logitech G Pro X Superlight 2", "Logitech", 159.99, "Wireless gaming mouse, HERO 25K sensor, 63g ultralight, LIGHTSPEED, 95hr battery", {"Sensor":"HERO 25K","Weight":"63g","Battery":"95hr","Wireless":"LIGHTSPEED"}, 4.8, 18234),
        ("Razer DeathAdder V3 Pro", "Razer", 149.99, "Wireless gaming mouse, Focus Pro 30K sensor, 90hr battery, 59g ergonomic", {"Sensor":"Focus Pro 30K","Battery":"90hr","Weight":"59g"}, 4.7, 12341),
        ("SteelSeries Prime Wireless", "SteelSeries", 129.99, "Wireless gaming mouse, TrueMove Air sensor, 100hr battery, magnetic charging", {"Sensor":"TrueMove Air","Battery":"100hr","Charging":"Magnetic"}, 4.6, 8923),
        ("Corsair K100 RGB", "Corsair", 229.99, "Mechanical gaming keyboard, Cherry MX Speed switches, RGB per-key, 4000Hz polling", {"Switches":"Cherry MX Speed","Polling":"4000Hz","Lighting":"RGB per-key"}, 4.7, 7234),
        ("Logitech G915 TKL Wireless", "Logitech", 229.99, "Wireless TKL mechanical keyboard, GL Low Profile switches, 40hr battery, RGB", {"Switches":"GL Low Profile","Wireless":"LIGHTSPEED + BT","Battery":"40hr"}, 4.7, 8923),
        ("Razer Huntsman V3 Pro", "Razer", 249.99, "Analog optical gaming keyboard, 8000Hz polling, Razer Snap Tap, RGB", {"Switches":"Analog Optical","Polling":"8000Hz","Feature":"Snap Tap"}, 4.7, 5234),
        ("LG UltraGear 27GR95QE OLED", "LG", 799.99, "27 inch QHD OLED gaming monitor, 240Hz, 0.03ms, G-Sync compatible, HDMI 2.1", {"Size":"27 inch","Panel":"OLED","Resolution":"QHD","Refresh":"240Hz","Response":"0.03ms"}, 4.9, 5234),
        ("ASUS ROG Swift Pro PG248QP", "ASUS", 899.99, "24.1 inch FHD esports monitor, 540Hz, Fast IPS, G-Sync, 0.2ms response", {"Size":"24.1 inch","Resolution":"FHD","Refresh":"540Hz","Response":"0.2ms"}, 4.8, 3421),
        ("Samsung Odyssey G9 49 inch", "Samsung", 1299.99, "49 inch super ultrawide OLED, 240Hz, 5120x1440, 0.03ms, G-Sync, HDMI 2.1", {"Size":"49 inch","Panel":"OLED","Resolution":"5120x1440","Refresh":"240Hz"}, 4.8, 4521),
        ("SteelSeries Arctis Nova Pro Wireless", "SteelSeries", 349.99, "Multi-system wireless gaming headset, ANC, hot-swap battery, Hi-Res certified", {"ANC":"Yes","Battery":"Hot-swap infinite","HiRes":"Yes"}, 4.7, 9234),
        ("PlayStation DualSense Edge", "Sony", 199.99, "Pro wireless PS5 controller, swappable sticks, back buttons, pro profiles", {"Sticks":"Swappable","Back Buttons":"Yes","Profiles":"Pro"}, 4.7, 18234),
        ("Xbox Elite Controller Series 2", "Microsoft", 179.99, "Pro Xbox controller, adjustable tension thumbsticks, wrap-around rubberized grip", {"Thumbsticks":"Adjustable tension","Paddles":"4 removable","Battery":"Rechargeable 40hr"}, 4.7, 23412),
        ("Scuf Reflex Pro", "Scuf", 219.99, "Pro PS5 controller, 4 removable paddles, instant triggers, rubberized grip", {"Paddles":"4 removable","Triggers":"Instant","Grip":"Rubberized"}, 4.5, 7234),
        ("Elgato Stream Deck MK.2", "Elgato", 149.99, "15 LCD key stream controller, customizable icons, plugin ecosystem, for streamers", {"Keys":"15 LCD","Plugins":"Thousands","Use":"Streaming/productivity"}, 4.8, 23412),
    ]
    for i, (name, brand, price, desc, specs, rating, reviews) in enumerate(gaming_products):
        products.append({"id": f"gaming_{i+1:03d}", "name": name, "brand": brand, "category": "gaming", "price": price, "description": desc, "specs": specs, "tags": ["gaming", brand.lower()], "rating": rating, "review_count": reviews, "in_stock": True})

    appliances = [
        ("Dyson V15 Detect Absolute", "Dyson", 749.99, "Cordless vacuum, laser dust detection, HEPA filtration, 60min runtime, LCD screen", {"Suction":"230 AW","Runtime":"60min","Filter":"HEPA","Detection":"Laser dust"}, 4.7, 12341),
        ("Dyson V12 Detect Slim", "Dyson", 649.99, "Slim cordless vacuum, laser detection, HEPA filter, 45min runtime, 2.2kg", {"Suction":"150 AW","Runtime":"45min","Filter":"HEPA","Weight":"2.2kg"}, 4.6, 9234),
        ("Dyson V11 Torque Drive", "Dyson", 499.99, "Cordless vacuum, intelligent suction, 60min runtime, LCD screen, HEPA", {"Suction":"185 AW","Runtime":"60min","Filter":"HEPA"}, 4.7, 18234),
        ("iRobot Roomba j9 Plus", "iRobot", 899.99, "Robot vacuum, auto-empty base, smart mapping, obstacle avoidance, self-cleaning brush", {"Mapping":"Smart","Auto-empty":"Yes","Navigation":"PrecisionVision"}, 4.6, 8923),
        ("Roborock S8 Pro Ultra", "Roborock", 1599.99, "Robot vacuum and mop combo, auto-empty, auto-wash mop, 6000Pa suction", {"Suction":"6000Pa","Mop":"Auto-wash","Auto-empty":"Yes"}, 4.7, 6234),
        ("Ecovacs Deebot X2 Omni", "Ecovacs", 1299.99, "Robot vacuum mop, auto-empty, hot air dry, 8000Pa, square brush, obstacle avoidance", {"Suction":"8000Pa","Mop":"Yes, hot dry","Auto-empty":"Yes"}, 4.6, 4521),
        ("Instant Pot Duo 7-in-1 6qt", "Instant Pot", 99.99, "7-in-1 electric pressure cooker, pressure cook, slow cook, rice cooker, steam, saute", {"Capacity":"6qt","Functions":"7-in-1","Programs":"13 smart"}, 4.7, 89234),
        ("Ninja Foodi MAX 14-in-1 7.5L", "Ninja", 249.99, "14-in-1 multi-cooker, pressure cook, air fry, steam, bake, grill, 7.5L capacity", {"Capacity":"7.5L","Functions":"14-in-1","Air Fry":"Yes"}, 4.7, 23412),
        ("Breville Barista Express", "Breville", 699.99, "Espresso machine with built-in grinder, 67 grind settings, steam wand, 2L tank", {"Grinder":"Built-in 67 settings","Pressure":"15 bar","Tank":"2L"}, 4.8, 34521),
        ("Breville Barista Pro", "Breville", 799.99, "Espresso machine with ThermoJet heating, 30-second heat up, integrated grinder", {"Heating":"ThermoJet 30sec","Grinder":"Integrated","Pressure":"15 bar"}, 4.8, 18234),
        ("Technivorm Moccamaster KBG 741", "Technivorm", 349.00, "Handmade coffee maker, SCAA certified, thermal carafe, brews 10 cups in 6min", {"Capacity":"40oz 10 cups","Brew Time":"6min","Carafe":"Thermal","Warranty":"5 years"}, 4.8, 7823),
        ("Nespresso Vertuo Next", "Nespresso", 179.99, "Capsule coffee machine, 5 cup sizes, 30sec heat-up, 1.1L tank, Bluetooth app", {"Sizes":"5 cup sizes","Heat-up":"30sec","Tank":"1.1L"}, 4.5, 45231),
        ("Nespresso OriginalLine Pixie", "Nespresso", 149.99, "Compact espresso machine, 19 bar, 1L tank, 25sec heat up, energy saving", {"Pressure":"19 bar","Tank":"1L","Heat-up":"25sec"}, 4.5, 34521),
        ("KitchenAid Artisan Stand Mixer 5qt", "KitchenAid", 449.99, "5qt stand mixer, 10 speeds, tilt-head, 3 attachments included, 325W motor", {"Capacity":"5qt","Speeds":"10","Power":"325W","Attachments":"3 included"}, 4.8, 67234),
        ("KitchenAid Professional 600 6qt", "KitchenAid", 599.99, "6qt professional stand mixer, bowl-lift, 10 speeds, 575W, for heavy doughs", {"Capacity":"6qt","Speeds":"10","Power":"575W","Type":"Bowl-lift"}, 4.8, 34521),
        ("Vitamix 5200 Blender", "Vitamix", 449.00, "Professional blender, 2HP motor, variable speed dial, 64oz container, 7 year warranty", {"Power":"2HP","Container":"64oz","Speeds":"Variable","Warranty":"7 years"}, 4.8, 45231),
        ("Ninja Mega Kitchen System", "Ninja", 159.99, "Blender food processor combo, 72oz pitcher, 8-cup processor, 1500W", {"Pitcher":"72oz","Processor":"8-cup","Power":"1500W","Functions":"Blend, process, drink"}, 4.6, 28234),
        ("Ninja Air Fryer Pro XL", "Ninja", 129.99, "6qt air fryer, 4-in-1, air fry roast reheat dehydrate, 400 degrees max", {"Capacity":"6qt","Functions":"4-in-1","Max Temp":"400°F"}, 4.7, 89234),
        ("COSORI Air Fryer 5.8qt", "COSORI", 99.99, "5.8qt air fryer, 100 recipes app, shake reminder, 11 preset modes, square basket", {"Capacity":"5.8qt","Presets":"11","App":"100 recipes"}, 4.6, 67234),
        ("Cuisinart 14-Cup Food Processor", "Cuisinart", 199.99, "14-cup food processor, 720W, slice dice chop puree, dishwasher safe parts", {"Capacity":"14-cup","Power":"720W","Functions":"Slice, dice, chop, puree"}, 4.7, 34521),
    ]
    for i, (name, brand, price, desc, specs, rating, reviews) in enumerate(appliances):
        products.append({"id": f"appliance_{i+1:03d}", "name": name, "brand": brand, "category": "home-appliances", "price": price, "description": desc, "specs": specs, "tags": ["appliance", "kitchen", brand.lower()], "rating": rating, "review_count": reviews, "in_stock": True})

    cameras = [
        ("Sony A7R V", "Sony", 3899.00, "61MP full-frame mirrorless, AI autofocus, 8-stop IBIS, 4K 60fps video, dual card slots", {"Sensor":"61MP full-frame","IBIS":"8-stop","Video":"4K 60fps","AF":"AI Subject Recognition"}, 4.9, 3421),
        ("Sony A7 IV", "Sony", 2499.00, "33MP full-frame mirrorless, 4K 60fps video, Real-time autofocus, 10fps burst shooting", {"Sensor":"33MP full-frame","Video":"4K 60fps","Burst":"10fps"}, 4.8, 8923),
        ("Sony A7C II", "Sony", 2299.00, "33MP full-frame compact mirrorless, AI autofocus, 4K 60fps, 5-axis IBIS", {"Sensor":"33MP full-frame","Video":"4K 60fps","Size":"Compact"}, 4.8, 5234),
        ("Sony A6700", "Sony", 1399.00, "26MP APS-C mirrorless, AI autofocus, 4K 120fps video, 5-axis IBIS, compact body", {"Sensor":"26MP APS-C","Video":"4K 120fps","IBIS":"5-axis"}, 4.7, 6234),
        ("Canon EOS R5 Mark II", "Canon", 4299.00, "45MP full-frame mirrorless, 8K RAW video, 30fps burst, IBIS, Dual Pixel AF II", {"Sensor":"45MP full-frame","Video":"8K RAW","Burst":"30fps"}, 4.9, 2341),
        ("Canon EOS R6 Mark II", "Canon", 2499.00, "24.2MP full-frame mirrorless, 4K 60fps, 40fps burst, IBIS, subject tracking AF", {"Sensor":"24.2MP full-frame","Video":"4K 60fps","Burst":"40fps"}, 4.8, 7234),
        ("Canon EOS R50", "Canon", 799.00, "24.2MP APS-C mirrorless, 4K video, Dual Pixel AF, compact beginner-friendly body", {"Sensor":"24.2MP APS-C","Video":"4K","AF":"Dual Pixel","Level":"Beginner"}, 4.6, 9234),
        ("Nikon Z8", "Nikon", 3999.00, "45.7MP full-frame mirrorless, 8K RAW video, 20fps burst, subject detection AF", {"Sensor":"45.7MP full-frame","Video":"8K RAW","Burst":"20fps"}, 4.9, 2134),
        ("Nikon Z6 III", "Nikon", 2499.00, "24.5MP full-frame mirrorless, 6K RAW video, 20fps burst, partially-stacked sensor", {"Sensor":"24.5MP full-frame","Video":"6K RAW","Burst":"20fps"}, 4.8, 4234),
        ("Nikon Z50 II", "Nikon", 949.00, "21MP APS-C mirrorless, 4K 30fps video, 11fps burst, vari-angle touchscreen", {"Sensor":"21MP APS-C","Video":"4K 30fps","Screen":"Vari-angle touch"}, 4.6, 6234),
        ("Fujifilm X-T5", "Fujifilm", 1699.00, "40.2MP APS-C mirrorless, 6.2K video, 15fps burst, IBIS, 20 film simulations", {"Sensor":"40.2MP APS-C","Video":"6.2K","Film Sim":"20 simulations"}, 4.8, 5234),
        ("Fujifilm X100VI", "Fujifilm", 1599.00, "40.2MP APS-C fixed lens compact, 6.2K video, IBIS, built-in ND filter, film simulations", {"Sensor":"40.2MP APS-C","Lens":"Fixed 23mm f/2","Video":"6.2K","IBIS":"6-stop"}, 4.9, 3421),
        ("Fujifilm X-S20", "Fujifilm", 1299.00, "26MP APS-C mirrorless, 6.2K video, vlogging-friendly, IBIS, film simulations", {"Sensor":"26MP APS-C","Video":"6.2K","Vlog":"Yes, flip screen"}, 4.7, 7234),
        ("OM System OM-5", "OM System", 999.00, "20.4MP MFT mirrorless, weather-sealed, 5-axis IBIS, 4K 30fps, compact adventure camera", {"Sensor":"20.4MP MFT","Sealed":"IP53","IBIS":"5-axis","Video":"4K 30fps"}, 4.6, 3421),
        ("GoPro Hero 13 Black", "GoPro", 399.99, "5.3K 60fps action camera, HyperSmooth 6.0 stabilization, HDR, 27MP photos, magnetic mounts", {"Video":"5.3K 60fps","Stabilization":"HyperSmooth 6.0","Photos":"27MP","Waterproof":"10m"}, 4.7, 18234),
        ("DJI Osmo Action 4", "DJI", 349.00, "4K 120fps action camera, 1/1.3-inch sensor, -20 degrees cold resistant, magnetic mount", {"Video":"4K 120fps","Sensor":"1/1.3-inch","Cold":"Operates at -20C"}, 4.7, 12341),
        ("DJI Mini 4 Pro", "DJI", 759.00, "249g drone, 4K 100fps, omnidirectional obstacle sensing, 34min flight, tri-directional", {"Video":"4K 100fps","Obstacle":"Omnidirectional","Flight":"34min","Weight":"249g"}, 4.8, 12341),
        ("DJI Air 3", "DJI", 1099.00, "Dual main cameras drone, 4K 100fps, 46min flight time, omnidirectional sensing", {"Cameras":"Dual main","Video":"4K 100fps","Flight":"46min"}, 4.8, 8923),
        ("Insta360 X4", "Insta360", 499.99, "360 degree 8K camera, 5.7K 60fps, AI editing, waterproof 10m, FlowState stabilization", {"Video":"8K 360 degree","Waterproof":"10m","Stabilization":"FlowState AI"}, 4.7, 6234),
        ("Polaroid Now Plus Gen 2", "Polaroid", 149.99, "i-Type instant camera, 5 creative lens filters, Bluetooth app control, double exposure", {"Film":"i-Type","Filters":"5 lens filters","Connectivity":"Bluetooth"}, 4.5, 8923),
    ]
    for i, (name, brand, price, desc, specs, rating, reviews) in enumerate(cameras):
        products.append({"id": f"camera_{i+1:03d}", "name": name, "brand": brand, "category": "cameras", "price": price, "description": desc, "specs": specs, "tags": ["camera", brand.lower(), "photography"], "rating": rating, "review_count": reviews, "in_stock": True})

    smarthome = [
        ("Amazon Echo Show 10 3rd Gen", "Amazon", 249.99, "10.1 inch HD smart display, rotating screen follows you, Alexa, smart home hub, video calls", {"Display":"10.1 inch HD","Rotation":"Motorized auto-rotate","Hub":"Zigbee/BT/WiFi"}, 4.6, 23412),
        ("Amazon Echo Show 8 3rd Gen", "Amazon", 149.99, "8 inch HD smart display, built-in Zigbee hub, Alexa, 13MP camera, spatial audio", {"Display":"8 inch HD","Camera":"13MP","Hub":"Zigbee built-in"}, 4.6, 34521),
        ("Amazon Echo Dot 5th Gen", "Amazon", 49.99, "Compact smart speaker with Alexa, improved bass, temperature sensor, eero WiFi built-in", {"Speaker":"1.73 inch","Sensor":"Temperature","WiFi":"eero mesh built-in"}, 4.7, 89234),
        ("Amazon Echo 4th Gen", "Amazon", 99.99, "Spherical smart speaker, premium sound, Alexa, Zigbee hub, eero WiFi mesh", {"Speaker":"3 inch woofer","Hub":"Zigbee","WiFi":"eero built-in"}, 4.7, 67234),
        ("Google Nest Hub Max 10 inch", "Google", 229.99, "10 inch smart display, Google Assistant, 6.5MP Nest Cam, ambient EQ display", {"Display":"10 inch","Camera":"6.5MP","Assistant":"Google","Gesture":"Yes"}, 4.6, 18234),
        ("Google Nest Hub 2nd Gen", "Google", 99.99, "7 inch smart display, Google Assistant, sleep sensing, ambient EQ, no camera", {"Display":"7 inch","Assistant":"Google","Sleep":"Sleep sensing sensor"}, 4.6, 34521),
        ("Google Nest Mini 2nd Gen", "Google", 49.99, "Compact smart speaker, Google Assistant, wall mount, recycled materials", {"Assistant":"Google","Mount":"Wall mountable","Material":"Recycled"}, 4.5, 56234),
        ("Apple HomePod 2nd Gen", "Apple", 299.00, "S9 chip, spatial audio, temperature and humidity sensor, Matter, Thread, Siri", {"Chip":"S9","Audio":"Spatial","Sensors":"Temp/Humidity","Protocol":"Matter, Thread"}, 4.7, 12341),
        ("Apple HomePod Mini", "Apple", 99.00, "S5 chip, 360 degree audio, temperature and humidity sensor, Ultra Wideband, Matter", {"Chip":"S5","Audio":"360 degree","Sensors":"Temp/Humidity","Protocol":"Matter"}, 4.6, 34521),
        ("Sonos Era 300", "Sonos", 449.00, "Spatial audio speaker, Dolby Atmos, Trueplay tuning, WiFi and Bluetooth, voice control", {"Audio":"Spatial Dolby Atmos","Tuning":"Trueplay auto","Connectivity":"WiFi + BT"}, 4.7, 8923),
        ("Philips Hue Starter Kit White and Color", "Philips", 199.99, "4x A19 color smart bulbs plus Hue Bridge, 16 million colors, voice and app control", {"Bulbs":"4x A19 1100lm","Colors":"16 million","Bridge":"Hue Bridge included"}, 4.7, 45231),
        ("Philips Hue Play Light Bar", "Philips", 99.99, "Gradient light bars for TV bias lighting, 16M colors, sync with entertainment", {"Type":"Gradient light bar","Colors":"16 million","Sync":"Entertainment sync"}, 4.6, 18234),
        ("Google Nest Learning Thermostat 4th Gen", "Google", 279.99, "Self-learning thermostat, Farsight HD color display, Matter protocol, energy history", {"Learning":"AI self-learning","Display":"Farsight HD color","Protocol":"Matter"}, 4.7, 18234),
        ("Ecobee SmartThermostat Premium", "Ecobee", 249.99, "Smart thermostat with built-in Alexa, air quality monitor, SmartSensor room sensor included", {"Assistant":"Alexa built-in","Sensor":"SmartSensor included","Air Quality":"Monitor"}, 4.7, 15234),
        ("Ring Video Doorbell Pro 2", "Ring", 249.99, "HD video doorbell, 3D motion detection, head-to-toe video, built-in Alexa, hardwired", {"Video":"1536p HD","Motion":"3D detection","Power":"Hardwired"}, 4.6, 34521),
        ("Ring Floodlight Cam Wired Pro", "Ring", 279.99, "Outdoor security camera with floodlights, 3D motion detection, two-way talk, Alexa", {"Video":"1080p HDR","Lights":"3000 lumen floodlights","Motion":"3D bird's eye"}, 4.6, 18234),
        ("Arlo Pro 5S 4K", "Arlo", 199.99, "Wireless 4K HDR security camera, color night vision, two-way audio, spotlight, IP67", {"Resolution":"4K HDR","Night Vision":"Color","Water":"IP67"}, 4.6, 12341),
        ("Wyze Cam v4", "Wyze", 35.99, "Budget 2K QHD security camera, color night vision, two-way audio, motion detection", {"Resolution":"2K QHD","Night Vision":"Color","Price":"Budget"}, 4.4, 67234),
        ("TP-Link Kasa Smart Plug EP25", "TP-Link", 24.99, "Smart plug with energy monitoring, voice control, away mode, compact design", {"Monitoring":"Energy usage","Voice":"Alexa/Google","Away Mode":"Yes"}, 4.6, 56234),
        ("Meross Smart Garage Door Opener", "Meross", 29.99, "Smart garage controller, works with HomeKit Alexa Google, remote open close monitoring", {"Compatibility":"HomeKit, Alexa, Google","Remote":"Yes","Alerts":"Open/close alerts"}, 4.5, 34521),
    ]
    for i, (name, brand, price, desc, specs, rating, reviews) in enumerate(smarthome):
        products.append({"id": f"smarthome_{i+1:03d}", "name": name, "brand": brand, "category": "smart-home", "price": price, "description": desc, "specs": specs, "tags": ["smart home", brand.lower(), "alexa", "google home"], "rating": rating, "review_count": reviews, "in_stock": True})

    wearables = [
        ("Apple Watch Ultra 2", "Apple", 799.00, "49mm titanium Apple Watch, S9 chip, 2000 nit Always-On display, 60hr battery, dive computer", {"Case":"49mm Titanium","Chip":"S9","Display":"2000 nit Always-On","Battery":"60hr","GPS":"Dual-frequency L1/L5"}, 4.8, 12341),
        ("Apple Watch Series 10 46mm", "Apple", 399.00, "46mm thinnest Apple Watch ever, S10 chip, sleep apnea detection, 18hr battery", {"Case":"46mm","Chip":"S10","Health":"Sleep apnea detection","Battery":"18hr"}, 4.8, 34521),
        ("Apple Watch Series 10 42mm", "Apple", 349.00, "42mm Apple Watch, S10 chip, sleep apnea detection, carbon neutral option", {"Case":"42mm","Chip":"S10","Health":"Sleep apnea detection"}, 4.8, 28234),
        ("Apple Watch SE 2nd Gen 44mm", "Apple", 249.00, "44mm Apple Watch SE, S8 chip, crash detection, fall detection, 50m swim-proof", {"Case":"44mm","Chip":"S8","Safety":"Crash and fall detection","Water":"50m"}, 4.7, 45231),
        ("Samsung Galaxy Watch 7 44mm", "Samsung", 299.99, "44mm Galaxy Watch, Exynos W1000, advanced BIA health sensor, sleep coaching, ECG", {"Case":"44mm","Chip":"Exynos W1000","Health":"BIA, ECG, BP","Battery":"40hr"}, 4.7, 18234),
        ("Samsung Galaxy Watch Ultra 47mm", "Samsung", 649.99, "47mm titanium Galaxy Watch Ultra, extreme sports tracking, dual-band GPS, 60hr battery", {"Case":"47mm Titanium","GPS":"Dual-band","Battery":"60hr","Sports":"Extreme tracking"}, 4.7, 8923),
        ("Garmin Fenix 8 Solar 51mm", "Garmin", 1099.99, "Multisport GPS watch with solar charging, AMOLED display option, 29 day battery, dive capable", {"GPS":"Multi-band GNSS","Battery":"29 days solar","Display":"AMOLED option","Dive":"Yes"}, 4.8, 6234),
        ("Garmin Forerunner 965", "Garmin", 599.99, "GPS running watch, AMOLED display, training load readiness, 31hr GPS battery, mapping", {"GPS":"Multi-band","Display":"AMOLED","Battery":"31hr GPS","Mapping":"Yes"}, 4.8, 8923),
        ("Garmin Venu 3", "Garmin", 449.99, "AMOLED smartwatch, sleep coaching, wheelchair mode, nap detection, 14 day battery", {"Display":"AMOLED","Battery":"14 days","Health":"Sleep coaching, nap detection"}, 4.7, 7234),
        ("Fitbit Charge 6", "Fitbit", 159.99, "Fitness tracker with built-in GPS, ECG, Google Maps, YouTube Music, 7-day battery", {"GPS":"Built-in","ECG":"Yes","Battery":"7 days","Google":"Maps, Wallet, TV"}, 4.5, 23412),
        ("Fitbit Inspire 3", "Fitbit", 99.99, "Slim fitness tracker, stress management, 10-day battery, sleep tracking, 20+ exercise modes", {"Battery":"10 days","Stress":"Score and tools","Sleep":"Sleep profile"}, 4.5, 34521),
        ("Whoop 4.0", "Whoop", 239.00, "Screenless health wearable, continuous HRV monitoring, strain and recovery scores, 5-day battery", {"Screen":"None","Monitoring":"24/7 HRV, strain","Battery":"5 days","Membership":"Monthly required"}, 4.6, 18234),
        ("Oura Ring Gen 3 Heritage", "Oura", 349.00, "Smart titanium ring, sleep and readiness tracking, 7-day battery, lightweight 4-6g", {"Form":"Ring","Material":"Titanium","Battery":"7 days","Weight":"4-6g"}, 4.6, 12341),
        ("Peloton Bike Plus", "Peloton", 2495.00, "Indoor cycling bike, 24 inch rotating HD touchscreen, Apple GymKit, auto-resistance following", {"Display":"24 inch HD rotating","Resistance":"Auto-follow","Compatibility":"Apple GymKit"}, 4.7, 8923),
        ("Bowflex SelectTech 552 Dumbbells Pair", "Bowflex", 429.00, "Adjustable dumbbells pair, 5 to 52.5 lbs each, 15 weight settings, replaces 15 pairs of weights", {"Weight Range":"5-52.5 lbs","Settings":"15 per dumbbell","Quantity":"Pair of 2"}, 4.7, 34521),
        ("NordicTrack Commercial 1750 Treadmill", "NordicTrack", 1799.00, "Smart treadmill, 14 inch HD touchscreen, iFit connected, 0 to 15 percent incline, negative 3 percent decline", {"Display":"14 inch HD","Speed":"0-12 mph","Incline":"0-15%","iFit":"1yr included"}, 4.6, 7234),
        ("Theragun Pro Gen 6", "Therabody", 599.00, "Percussive therapy massage gun, 60 lbs force, 6 speed settings, OLED screen, app connected", {"Force":"60 lbs","Speeds":"6","Display":"OLED","App":"Therabody app"}, 4.7, 12341),
        ("Hyperice Hypervolt 2 Pro", "Hyperice", 329.00, "Percussion massage gun, QuietGlide technology, 3 speeds, 5 attachments, Bluetooth app", {"Technology":"QuietGlide","Speeds":"3","Attachments":"5","Connectivity":"Bluetooth"}, 4.6, 9234),
        ("Garmin Index S2 Smart Scale", "Garmin", 149.99, "Wi-Fi smart scale, BMI, body fat, muscle mass, bone mass, syncs to Garmin Connect", {"Metrics":"Weight, BMI, body fat, muscle, bone","Connectivity":"Wi-Fi","Sync":"Garmin Connect"}, 4.6, 8234),
        ("Withings Body Comp Scale", "Withings", 199.95, "Body composition scale, visceral fat, vascular age, nerve health, ECG, Wi-Fi", {"Metrics":"Visceral fat, vascular age, nerve health","ECG":"Yes","Connectivity":"Wi-Fi + BT"}, 4.6, 6234),
    ]
    for i, (name, brand, price, desc, specs, rating, reviews) in enumerate(wearables):
        products.append({"id": f"wear_{i+1:03d}", "name": name, "brand": brand, "category": "wearables", "price": price, "description": desc, "specs": specs, "tags": ["wearable", brand.lower(), "fitness", "health"], "rating": rating, "review_count": reviews, "in_stock": True})

    office = [
        ("Apple iPad Pro M4 13 inch", "Apple", 1299.00, "M4 chip, 13 inch Ultra Retina XDR Tandem OLED, up to 2TB storage, Apple Pencil Pro support", {"Chip":"M4","Display":"13 inch Tandem OLED","Storage":"Up to 2TB","Pencil":"Apple Pencil Pro"}, 4.9, 8923),
        ("Apple iPad Pro M4 11 inch", "Apple", 999.00, "M4 chip, 11 inch Ultra Retina XDR Tandem OLED, thin light design, Apple Pencil Pro", {"Chip":"M4","Display":"11 inch Tandem OLED","Pencil":"Apple Pencil Pro"}, 4.8, 12341),
        ("Apple iPad Air M2 13 inch", "Apple", 799.00, "M2 chip, 13 inch Liquid Retina, 8GB RAM, landscape front camera, Apple Pencil Pro", {"Chip":"M2","Display":"13 inch Liquid Retina","RAM":"8GB","Camera":"Landscape orientation"}, 4.8, 15234),
        ("Apple iPad Air M2 11 inch", "Apple", 599.00, "M2 chip, 11 inch Liquid Retina, 8GB RAM, USB-C, Apple Pencil Pro support", {"Chip":"M2","Display":"11 inch Liquid Retina","RAM":"8GB"}, 4.8, 23412),
        ("Apple iPad 10th Gen", "Apple", 349.00, "A14 Bionic chip, 10.9 inch Liquid Retina, landscape camera, USB-C, 5G option", {"Chip":"A14 Bionic","Display":"10.9 inch Liquid Retina","Connector":"USB-C"}, 4.7, 45231),
        ("Samsung Galaxy Tab S10 Ultra", "Samsung", 1199.99, "14.6 inch Dynamic AMOLED 2X, Snapdragon 8 Gen 3, S Pen included, DeX desktop mode", {"Display":"14.6 inch AMOLED 2X","S Pen":"Included","RAM":"12GB","Mode":"DeX desktop"}, 4.7, 6234),
        ("Samsung Galaxy Tab S10 Plus", "Samsung", 999.99, "12.4 inch Dynamic AMOLED 2X, Snapdragon 8 Gen 3, S Pen, DeX mode, IP68 waterproof", {"Display":"12.4 inch AMOLED 2X","S Pen":"Included","Water":"IP68"}, 4.7, 8923),
        ("Dell UltraSharp U2723QE 27 inch", "Dell", 799.99, "27 inch 4K IPS Black monitor, USB-C 90W, 100 percent sRGB, factory calibrated, pivot stand", {"Size":"27 inch","Resolution":"4K UHD","Panel":"IPS Black","USB-C":"90W Power Delivery"}, 4.8, 7234),
        ("LG UltraFine 5K 27 inch", "LG", 1299.99, "27 inch 5K resolution IPS, Thunderbolt 3, 500 nit, P3 wide color, ideal for Mac", {"Size":"27 inch","Resolution":"5120x2880 5K","Connector":"Thunderbolt 3","Color":"P3 wide"}, 4.7, 5234),
        ("BenQ PD3220U 32 inch", "BenQ", 1099.99, "32 inch 4K USB-C monitor, Thunderbolt 3, Pantone validated color, daisy chain", {"Size":"32 inch","Resolution":"4K","Connector":"Thunderbolt 3","Color":"Pantone validated"}, 4.7, 4234),
        ("Samsung 34 inch Ultrawide Curved", "Samsung", 799.99, "34 inch ultrawide curved monitor, 3440x1440 resolution, 165Hz, 1ms, USB-C 90W", {"Size":"34 inch","Resolution":"3440x1440","Refresh":"165Hz","Curve":"1000R"}, 4.7, 8923),
        ("Logitech MX Keys S Wireless Keyboard", "Logitech", 109.99, "Wireless keyboard, smart backlight, Easy-Switch 3 devices, USB-C, 10-day battery", {"Wireless":"Bluetooth + Logi Bolt","Devices":"3 Easy-Switch","Battery":"10 days backlit"}, 4.7, 23412),
        ("Logitech MX Master 3S Mouse", "Logitech", 99.99, "Wireless mouse, MagSpeed electromagnetic scroll, 8K DPI, silent clicks, multi-device", {"Sensor":"8K DPI","Scroll":"MagSpeed","Devices":"3","Silent":"Yes"}, 4.8, 34521),
        ("Apple Magic Keyboard with Touch ID", "Apple", 149.00, "Wireless Mac keyboard, Touch ID fingerprint, USB-C charging, scissor mechanism keys", {"Connectivity":"Bluetooth","Auth":"Touch ID","Charging":"USB-C","Keys":"Scissor mechanism"}, 4.7, 28234),
        ("Apple Magic Mouse", "Apple", 79.00, "Wireless Mac mouse, Multi-Touch surface, USB-C charging, smooth glide", {"Connectivity":"Bluetooth","Surface":"Multi-Touch","Charging":"USB-C"}, 4.3, 34521),
        ("FlexiSpot E7 Pro Standing Desk", "FlexiSpot", 599.99, "Dual motor standing desk, 355 lbs capacity, 22.8 to 48.4 inch height, programmable memory, anti-collision", {"Motor":"Dual brushless","Capacity":"355 lbs","Height":"22.8-48.4 inch","Warranty":"15-year frame"}, 4.6, 3789),
        ("Uplift V2 Commercial Standing Desk", "Uplift", 799.00, "Commercial grade standing desk, 355 lbs capacity, dual motor, 7-year warranty, ANSI BIFMA certified", {"Motor":"Dual","Capacity":"355 lbs","Warranty":"7 years","Certification":"ANSI/BIFMA"}, 4.7, 5234),
        ("Herman Miller Aeron Chair Size C", "Herman Miller", 1795.00, "Premium ergonomic office chair, PostureFit SL lumbar, 8Z Pellicle mesh, 8D armrests, 12-year warranty", {"Lumbar":"PostureFit SL","Mesh":"8Z Pellicle","Armrests":"8D","Warranty":"12 years"}, 4.9, 8923),
        ("Steelcase Leap V2 Chair", "Steelcase", 1699.00, "Premium ergonomic office chair, LiveBack adaptive technology, natural glide system, 12-year warranty", {"Back":"LiveBack adaptive","Glide":"Natural glide","Arms":"4D adjustable","Warranty":"12 years"}, 4.8, 6234),
        ("Secretlab Titan Evo 2022 XL", "Secretlab", 549.00, "Gaming and office chair, 4D magnetic armrests, L-adapt lumbar, NAPA leather or SoftWeave fabric", {"Armrests":"4D magnetic","Lumbar":"L-adapt pebble","Material":"NAPA or SoftWeave"}, 4.7, 12341),
    ]
    for i, (name, brand, price, desc, specs, rating, reviews) in enumerate(office):
        products.append({"id": f"office_{i+1:03d}", "name": name, "brand": brand, "category": "office", "price": price, "description": desc, "specs": specs, "tags": ["office", brand.lower(), "productivity"], "rating": rating, "review_count": reviews, "in_stock": True})

    return products


async def seed():
    products = generate_products()
    print(f"🌱 Seeding {len(products)} products across 10 categories...")
    batch_size = 30
    total_chunks = 0
    total_ingested = 0
    async with httpx.AsyncClient(timeout=120.0) as client:
        for i in range(0, len(products), batch_size):
            batch = products[i:i + batch_size]
            resp = await client.post(
                "http://localhost:8000/api/v1/products/ingest",
                json={"products": batch},
            )
            resp.raise_for_status()
            data = resp.json()
            total_chunks += data.get("chunk_count", 0)
            total_ingested += len(batch)
            print(f"  ✅ Batch {i//batch_size + 1}: {total_ingested}/{len(products)} products done")

    print(f"\n🎉 Complete! {len(products)} products → {total_chunks} chunks stored in ChromaDB")
    print(f"\nCategories seeded:")
    from collections import Counter
    cats = Counter(p['category'] for p in products)
    for cat, count in sorted(cats.items()):
        print(f"  📦 {cat}: {count} products")


if __name__ == "__main__":
    asyncio.run(seed())
