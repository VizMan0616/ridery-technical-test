{
    "name": "Gestión de Vehículos",
    "summary": """
        Permite la gestión de vehículos y asociación a contactos.
    """,
    "author": "José Vizcaya",
    "category": "Contact/Fleet",
    "version": "16.0.1.2.0",
    "depends": ["contacts", "endpoint_logs"],
    "data": [
        "security/fleet_management_security.xml",
        "security/ir.model.access.csv",
        "data/data.xml",
        "views/res_partner_views.xml",
        "views/vehicle_views.xml",
        "views/vehicle_brand_views.xml",
        "views/vehicle_management_menuitem.xml",
    ],
    "application": True,
}
