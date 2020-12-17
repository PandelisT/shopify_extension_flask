from controllers.auth_controller import auth
from controllers.customer_controller import customer
from controllers.note_controller import note
from controllers.tag_controller import tag
from controllers.habit_controller import habit
from controllers.order_controller import order
from controllers.product_controller import product
from controllers.article_controller import article
from controllers.address_controller import address



registerable_controllers = [
    auth,
    customer,
    note,
    tag,
    habit,
    order,
    product,
    article,
    address
]
