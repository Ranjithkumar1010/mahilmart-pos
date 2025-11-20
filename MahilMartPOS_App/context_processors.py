from .models import AdminSettings, CashierPermission, SupervisorPermission
from .models import CashierPermission, SupervisorPermission

def user_permissions(request):
    # If the user is not logged in → don't query the DB
    if not request.user.is_authenticated:
        return {"perm": None}

    # Import models locally (prevents circular import issues)
    from .models import SupervisorPermission, CashierPermission

    user = request.user

    # Superuser always bypasses permissions
    if user.is_superuser:
        return {"perm": None}

    # Staff → Supervisor permissions
    if user.is_staff:
        perm = SupervisorPermission.objects.filter(user_id=user.id).first()
    else:
        # Normal user → Cashier permissions
        perm = CashierPermission.objects.filter(user_id=user.id).first()

    return {"perm": perm}



def base_context(request):
    theme = AdminSettings.objects.first()

    user = request.user
    perm = None

    if user.is_authenticated:

        # Superadmin always full permission
        if user.is_superuser:
            class FullPerm:
                allow_dashboard = True
                allow_billing = True
                allow_sales_return = True
                allow_products = True
                allow_items = True
                allow_purchase = True
                allow_inventory = True
                allow_suppliers = True
                allow_config_view = True
                allow_barcodes = True
                allow_reports = True
                allow_logs = True
                allow_company = True
                allow_customers = True
                allow_payments = True
                allow_expenses = True
                allow_settings = True
            perm = FullPerm()

        # Supervisor
        elif user.is_staff:
            perm = SupervisorPermission.objects.filter(user=user).first()

        # Cashier
        else:
            perm = CashierPermission.objects.filter(user=user).first()

    # No permission found → dummy all false
    if perm is None:
        class DummyPerm:
            allow_dashboard = False
            allow_billing = False
            allow_sales_return = False
            allow_products = False
            allow_items = False
            allow_purchase = False
            allow_inventory = False
            allow_suppliers = False
            allow_config_view = False
            allow_barcodes = False
            allow_reports = False
            allow_logs = False
            allow_company = False
            allow_customers = False
            allow_payments = False
            allow_expenses = False
            allow_settings = False
        perm = DummyPerm()

    return {
        "theme": theme,
        "perm": perm,
    }
