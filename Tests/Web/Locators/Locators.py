##--Url--##
url                 = "https://admin-demo.nopcommerce.com/Admin"

##--Login--##
Login_button_id     = '//*[@class="button-1 login-button"]'

##--Catalog--##
Catalog_button_id   = '//*[contains(text(),"Catalog")]'

##--Products--##
Product_button_id   = '//*[contains(text(),"Products")]'
Add_new_p           = 'https://admin-demo.nopcommerce.com/Admin/Product/Create'
Prod_name           = '//*[@data-val-required="Please provide a name."]'
Save                = '//*[@name="save"]'
Search_Prod         = '//*[@name="SearchProductName"]'
Search_res          = '//*[@id="products-grid"]'
Search_btn          = '//*[@id="search-products"]'
Download_Prod       = '//*[@name="download-catalog-pdf"]'
Export_hover        = '//*[@class="btn btn-success dropdown-toggle"]'
Export_Excel        = '//*[@name="exportexcel-all"]'
Import              = '//*[@name="importexcel"]'
Import_Excel        = '//*[@name="importexcel"]'
Checkbox            = '//*[@id="products-grid"]/tbody/tr[1]/td[1]/input'
Delete_Selected     = '//*[@id="delete-selected"]' 

##--Categories--##
Categories_button_id = '//*[contains(text(),"Categories")]'
Add_new_Cat          = ' https://admin-demo.nopcommerce.com/Admin/Category/Create'
Search_Cat           = '//*[@id="SearchCategoryName"]'
Search_res_Cat       = '//*[@id="categories-grid"]'
Search_btn_Cat       = '//*[@id="search-categories"]'
Export_Excel_Cat     = 'https://admin-demo.nopcommerce.com/Admin/Category/ExportXlsx'
Checkbox_cat         = '//*[@id="categories-grid"]/tbody/tr/td[1]/input'

##--Manufacturers--##
Manufacturers_button_id = '//*[contains(text(),"Manufacturers")]'
Add_new_Man             = 'https://admin-demo.nopcommerce.com/Admin/Manufacturer/Create'
Search_Man              = '//*[@name="SearchManufacturerName"]'
Search_res_Man          = '//*[@id="manufacturers-grid"]'
Search_btn_Man          = '//*[@id="search-manufacturers"]'
Export_Excel_Man        = 'https://admin-demo.nopcommerce.com/Admin/Manufacturer/ExportXlsx'
Checkbox_Man            = '//*[@id="manufacturers-grid"]/tbody/tr/td[1]/input'
Delete_Selected         = '//*[@id="delete-selected"]' 

##--Reviews--##
Reviews_button_id       =   '//*[contains(text()," Product reviews")]'     
Search_Review           =   '//*[@id="CreatedOnFrom"]'
Search_btn_Review       =   '//*[@id="search-productreviews"]'
Checkbox_Review         =   '//*[@id="productreviews-grid"]/tbody/tr[1]/td[1]/input'
Checkbox_Review2        =   '//*[@id="productreviews-grid"]/tbody/tr[6]/td[1]/input'
Approve_Review          =   '//*[@id="approve-selected"]'
Disapprove_Review       =   '//*[@id="disapprove-selected"]'
Wait_for_Review         =   '//*[@id="productreviews-grid"]'
Delete_Selected_R       =   '//*[@id="delete-selected"]' 
yes                     =   '//*[@id="delete-selected-action-confirmation-submit-button"]'
ok                      =   '(//*[@data-dismiss="modal"])[4]'

##--Tags--##
Tags_button_id          =  '//*[contains(text(),"Product tags")]'
Search_tags             =  '//*[@name="SearchTagName"]'
Search_res_tags         =  '//*[@id="product-tags-grid"]'
Search_btn_tags         =  '//*[@id="search-product-tags"]'
Checkbox_Tags           =  '//*[@id="product-tags-grid"]/tbody/tr[1]/td[1]/input'

##--Attributes--##
Attributes              =  '//*[contains(text(),"Attributes")]'

##--Product--Attributes--##
Product_att             =  '//*[contains(text()," Product attributes")]'
Add_new_pa              =  'https://admin-demo.nopcommerce.com/Admin/ProductAttribute/Create' 
Checkbox_pa             =  '//*[@id="products-grid"]/tbody/tr[1]/td[1]/input'

##--Specification--Attributes--##
Specification_att   =    '//*[contains(text()," Specification attributes")]'
Add_new_sa          =    'https://admin-demo.nopcommerce.com/Admin/SpecificationAttribute/CreateSpecificationAttribute'
Checkbox_sa         =    '//*[@id="child0_specificationattributegroups_grid"]/tbody/tr[1]/td[1]/input'
Grp_Hover           =    '//*[@id="specificationattributegroups-grid"]/tbody/tr[1]/td[1]'
Delete_Selected_Sa  =    '//*[@id="delete-selected-specification-attributes"]'
yes_sa              =    '//*[@id="delete-selected-specification-attributes-action-confirmation-submit-button"]'

##--Checkout--Attributes--##
Checkout_att    =   '//*[contains(text()," Checkout attributes")]'
Add_new_Ca      =   'https://admin-demo.nopcommerce.com/Admin/CheckoutAttribute/Create'
Checkbox_Ca     =   '//*[@id="checkoutattributes-grid"]/tbody/tr/td[1]/input'