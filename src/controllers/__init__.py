from controllers.auth_controller import auth
from controllers.customer_controller import customer
from controllers.note_controller import note
from controllers.tag_controller import tag
from controllers.habit_controller import habit


registerable_controllers = [
    auth,
    customer,
    note,
    tag,
    habit
]