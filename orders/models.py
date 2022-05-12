from django.db import models

# Create your models here.
class Order(models.Model):
    def __str__(self) -> str:
        return f"{self.item_name} * {self.item_quantity} by {self.user_id} on {self.order_date} cost={self.order_cost}"
    # auto fields
    order_id = models.AutoField(primary_key=True)
    order_date = models.DateField(auto_now_add=True)
    # from current user
    user_id = models.CharField(default="null", max_length=20)
    # finger print img
    f_print=models.TextField(default="null")
    # item info 
    item_name=models.CharField(max_length=20)
    item_id=models.CharField(max_length=20)
    item_rate=models.CharField(max_length=20)
    # order info
    item_quantity=models.CharField(max_length=2)
    # qunatity*rate
    order_cost=models.CharField(max_length=20)