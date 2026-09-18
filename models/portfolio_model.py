class PortfolioModel:
    @staticmethod
    def get_hero_slides():
        return [
            {"image": "hero1.webp", "title": "Where Creativity Meets Comfort", "subtitle": "Custom Modular Kitchens & Architectural Home Interiors", "btn_type": "whatsapp"},
            {"image": "hero2.webp", "title": "20+ Years of Craftsmanship", "subtitle": "Built with Century Club Prime Plywood & Original Hettich Hardware", "btn_type": "call"},
        ]

    @staticmethod
    def get_services():
        return [
            {"title": "Modular Kitchens", "description": "Custom acrylic, laminate, and PU finishes engineered with authentic Hettich soft-close hardware.", "icon": "fa-kitchen-set"},
            {"title": "Bespoke Wardrobes", "description": "Floor-to-ceiling sliding and hinged wardrobe systems built with Century Club Prime 30-year warranty ply.", "icon": "fa-door-closed"},
            {"title": "Living & TV Units", "description": "Architectural media walls, acoustic louvers, and custom storage solutions designed for modern Kolkata homes.", "icon": "fa-tv"},
        ]

    @staticmethod
    def get_gallery_items():
        return [
            {"title": "L-Shaped Acrylic Modular Kitchen", "image": "hero1.webp", "category": "kitchen"},
            {"title": "Floor-to-Ceiling Sliding Glass Wardrobe", "image": "hero2.webp", "category": "wardrobe"},
            {"title": "Modern TV Console Unit", "image": "hero1.webp", "category": "living"},
        ]