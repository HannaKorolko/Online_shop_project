var product_img= [document.getElementById('wareniki_img'), document.getElementById('golubci_img'),
    document.getElementById('syrniki_img'), document.getElementById('pancakes_img')]
var list_of_img = document.getElementById("menu_of_store")
var src_1st_img_wareniki = "https://smachno.ua/wp-content/uploads/2012/05/10/varenikiskapustoj.jpg"
var src_2nd_img_wareniki = "https://pelmeshki.od.ua/wa-data/public/shop/products/23/00/23/images/46/46.970.jpg"
var src_1st_img_golubci = "https://www.recept.ua/files/uploads/rec_img/golubci-iz-svegey-kapusti.jpg"
var src_2nd_img_golubci = "https://www.home-recipes.com.ua/wp-content/uploads/2021/04/golubcy-mjasnye-e6bada4.jpg"
var src_1st_img_syrniki = "https://sites.psu.edu/jsc5483/wp-content/uploads/sites/16465/2014/09/2482222_orig.jpg"
var src_2nd_img_syrniki = "https://clutch.net.ua/crops/6c367e/1200x1200/2/0/2021/03/31/XMqbZLW46e8eRbfBuDpDNIaU3LjsA2WO3CGUgQLl.jpeg"
var src_1st_img_pancakes = "https://shuba.life/static/content/thumbs/320x400/6/84/mwffoq---c320x400x50px50p-c320x400x50px50p-up--49e5669f372936d02bc2ae1b3ef36846.jpg"
var src_2nd_img_pancakes = "http://gurman.co.ua/wp-content/uploads/2017/01/8ba692ae40904ed3030417525ff16379.jpg"

var src_1st_img_product = [src_1st_img_wareniki, src_1st_img_golubci, src_1st_img_syrniki, src_1st_img_pancakes]
var src_2nd_img_product = [src_2nd_img_wareniki, src_2nd_img_golubci, src_2nd_img_syrniki, src_2nd_img_pancakes]

    list_of_img.addEventListener('click', e => {

        for (i=0; i<product_img.length; i++) {
            if (e.target === product_img[i]) {
                if (product_img[i].src === src_1st_img_product[i]) {
                    product_img[i].src = src_2nd_img_product[i]
                } else  {
                    product_img[i].src = src_1st_img_product[i]      
        }}}   
})
