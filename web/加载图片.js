// 加载图片
function loadingImg(arr_imgs) {
    console.log("start loading img....");
    console.log(arr_imgs);
    for (var i = 0; i < arr_imgs.length; i++) {
        loadImageWithIndex(i, arr_imgs);
    };
};

var loadimgcount=0;
function loadImageWithIndex(vindex, arr_imgs) {
    setTimeout(function(){
        var _tmp_source;
        _tmp_source = new Image();
        _tmp_source.src = arr_imgs[vindex];
        _tmp_source.onload = function () {
            loadimgcount++;
            console.log("loading finish:" + arr_imgs[vindex]);
            if (loadimgcount == arr_imgs.length) {
            	console.log("load finish all images...");
            	// doing something...

                // setTimeout(function () {
                //     setTimeout(function(){
                //     	// doing something...
                //     },200);
                // }, 2500);
            }
        }
    },10)
};