/*non clustered index1 on inventory module*/
USE INVENTORYMODULE;

create nonclustered index ix_products_productName on products(productName)

/*non clustered index2 on inventory module*/
create nonclustered index ix_supplier_supplierName on suppliers(supplierName)

/*non clustered index1 on library management*/
use librarymanagement
create nonclustered index ix_books_title on books(title)

/*non clustered index2 on library management*/
create nonclustered index ix_authors_firstName on authors(firstName)

/*non clustered index1 on social media app*/
use socialmediaapp
create nonclustered index ix_users_userName on users(userName)

/*non clustered index2 on library management*/
create nonclustered index ix_users_email on users(email)