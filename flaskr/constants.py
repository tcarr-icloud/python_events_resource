# Shopping Cart Events
# These events focus on user interaction with the shopping cart before the final transaction:
CREATE_CART = {'event': "Create Cart", 'description': "A user creates a cart."}
ITEM_ADDED_TO_CART = {'event': "Item Added to Cart",
                      'description': "A product is successfully added to the user's cart."}
ITEM_REMOVED_FROM_CART = {'event': "Item Removed from Cart",
                          'description': "A product is taken out of the shopping cart by the user."}
CART_VIEWED = {'event': "Cart Viewed", 'description': "The user views the contents of their cart."}
UPDATE_CART = {'event': "Update Cart",
               'description': "The user modifies the quantity or configuration of items within the cart."}
APPLY_PROMOTION_DISCOUNT = {'event': "Apply Promotion/Discount",
                            'description': "A user applies a discount code or promotion to their order."}
INITIATE_CHECKOUT_CHECKOUT_STARTED = {'event': "Initiate Checkout/Checkout Started",
                                      'description': "The user begins the process of completing their order."}

# Order Events
# These events relate to the steps involved in completing a purchase and post-purchase activities:
CHECKOUT_STEP_VIEWED_COMPLETED = {'event': "Checkout Step Viewed/Completed",
                                  'description': "The user navigates through specific stages of the checkout (e.g., entering shipping information, selecting a payment method)."}
ORDER_PLACED_PURCHASED = {'event': "Order Placed/Purchased",
                          'description': "The transaction is successfully completed, and an order is created."}
PAYMENT_SUCCESS_FAILED = {'event': "Payment Success/Failed",
                          'description': "The status of the payment transaction is recorded."}
ORDER_CONFIRMED = {'event': "Order Confirmed",
                   'description': "The system confirms the order details and notifies the user."}
ORDER_SHIPPED = {'event': "Order Shipped",
                 'description': "The physical items in the order have been dispatched for delivery."}
ORDER_DELIVERED = {'event': "Order Delivered", 'description': "The items have reached the customer."}
REFUND_ISSUED = {'event': "Refund Issued", 'description': "A full or partial refund is processed for the order."}
ORDER_CANCELLED = {'event': "Order Cancelled", 'description': "The order is cancelled before fulfillment."}

# Common Associated Events
# Other events often tracked alongside the core cart and order events for analytics and user experience improvement include:
PRODUCT_VIEWED = {'event': "Product Viewed",
                  'description': "A user views the detailed page of an item, indicating interest."}
PRODUCT_SEARCHED = {'event': "Product Searched",
                    'description': "A user uses the search function to find specific products."}
ADD_TO_WISHLIST = {'event': "Add to Wishlist", 'description': "A user saves an item for later consideration."}
CART_ABANDONMENT = {'event': "Cart Abandonment",
                    'description': "The user leaves the site or closes the cart without completing the purchase."}
