var imgProductSrc = [document.getElementById('vareniki-img'), document.getElementById('golubci-img'),
    document.getElementById('syrniki-img'), document.getElementById('pancakes-img')]
var menu = document.getElementById("menu-of-shop")
var varenikImg = {
    1: "https://smachno.ua/wp-content/uploads/2012/05/10/varenikiskapustoj.jpg",
    2: "https://pelmeshki.od.ua/wa-data/public/shop/products/23/00/23/images/46/46.970.jpg"
}    
var golubecImg = {
    1: "https://www.recept.ua/files/uploads/rec_img/golubci-iz-svegey-kapusti.jpg",
    2: "https://www.home-recipes.com.ua/wp-content/uploads/2021/04/golubcy-mjasnye-e6bada4.jpg"
}
var syrnikImg = {
    1: "https://sites.psu.edu/jsc5483/wp-content/uploads/sites/16465/2014/09/2482222_orig.jpg",
    2: "https://clutch.net.ua/crops/6c367e/1200x1200/2/0/2021/03/31/XMqbZLW46e8eRbfBuDpDNIaU3LjsA2WO3CGUgQLl.jpeg"
}    
var pancakeImg = {
    1: "https://shuba.life/static/content/thumbs/320x400/6/84/mwffoq---c320x400x50px50p-c320x400x50px50p-up--49e5669f372936d02bc2ae1b3ef36846.jpg",
    2: "http://gurman.co.ua/wp-content/uploads/2017/01/8ba692ae40904ed3030417525ff16379.jpg"
}
var productImg = [varenikImg, golubecImg, syrnikImg, pancakeImg]

menu.addEventListener('click', e => {
    for (i=0; i<imgProductSrc.length; i++) {
            if (e.target === imgProductSrc[i]) {
                if (imgProductSrc[i].src === productImg[i][1]) {
                    imgProductSrc[i].src = productImg[i][2]
                }
                else  {
                    imgProductSrc[i].src = productImg[i][1]
                }                
            }
    }   
})
