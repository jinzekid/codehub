//get all images in style（此方法引用其他博客的）
function getallBgimages() {
    var url, B = [], A = document.getElementsByTagName('*');
    A = B.slice.call(A, 0, A.length);
    while (A.length) {
        url = document.deepCss(A.shift(), 'background-image');
        if (url) url = /url\(['"]?([^")]+)/.exec(url) || [];
        url = url[1];
        if (url && B.indexOf(url) == -1) B[B.length] = url;
    }
    return B;
}

var pre_images      = new Array();
var loadimgcount    = 0;
function preLoadImg() {
    //第一种方式：通过dom方法获取页面中的所有img，包括<img>标签和css中的background-image
    //get all imgs those tag is <img>
    var imgs = document.images;
    for (var i = 0; i < imgs.length; i++) {
        pre_images.push(imgs[i].src);
    }
    //get all images in style
    var cssImages = getallBgimages();
    for (var j = 0; j < cssImages.length; j++) {
        pre_images.push(cssImages[j]);
    }

    for (var i = pre_images.length - 1; i >= 0; i--) {
        console.log("img:" + pre_images[i]);
    }

    console.log("preloadingimg:" + pre_images);
    console.log("preloadingimg length:" + pre_images.length);

    loadimgcount = 0;
    loadingImg(pre_images);
}