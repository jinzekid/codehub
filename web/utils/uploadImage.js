function upload_obj(fileObj, do_success_uploadimg, do_failed_uploadimg, func_complete) { 
  var file = fileObj; 
  //图片方向角 added by lzk 
  var Orientation = null; 
    
  if (file) { 
    console.log("正在上传,请稍后..."); 
    var rFilter = /^(image\/jpeg|image\/png)$/i; // 检查图片格式 
    if (!rFilter.test(file.type)) { 
      //showMyTips("请选择jpeg、png格式的图片", false); 

      upload_video_obj(file, do_success_uploadimg, do_failed_uploadimg, func_complete);
      return; 
    } 


    // 如果是图片就是上传
    upload_img_obj(file, do_success_uploadimg, do_failed_uploadimg, func_complete);
  }


}

function selectFileImageToUpload(fileObj, do_success_uploadimg, do_failed_uploadimg) { 
  var file = fileObj.files[0]; 
  //图片方向角 added by lzk 
  var Orientation = null; 
    
  if (file) { 
    console.log("正在上传,请稍后..."); 
    var rFilter = /^(image\/jpeg|image\/png)$/i; // 检查图片格式 
    if (!rFilter.test(file.type)) { 
      //showMyTips("请选择jpeg、png格式的图片", false); 
      return; 
    } 
    // var URL = URL || webkitURL; 
    //获取照片方向角属性，用户旋转控制 
    EXIF.getData(file, function() { 
      // alert(EXIF.pretty(this)); 
      EXIF.getAllTags(this);  
      //alert(EXIF.getTag(this, 'Orientation'));  
      Orientation = EXIF.getTag(this, 'Orientation'); 
      //return; 
    }); 
      
    var oReader = new FileReader(); 
    oReader.onload = function(e) { 
      //var blob = URL.createObjectURL(file); 
      //_compress(blob, file, basePath);

      var URL = window.URL && window.URL.createObjectURL ? window.URL : window.webkitURL && window.webkitURL.createObjectURL ? window.webkitURL : null;
      var src = URL.createObjectURL(file);

      var image = new Image(); 
      image.src = src;//e.target.result; 
      image.onload = function() { 
        var that = this;
        var canvas = document.createElement("canvas"); 
        // 图片原始尺寸
        var originWidth = this.width;
        var originHeight = this.height;
        // 最大尺寸限制，可通过国设置宽高来实现图片压缩程度
        var maxWidth = 800,
            maxHeight = 800;
        // 目标尺寸
        var targetWidth = originWidth,
            targetHeight = originHeight;
        // 图片尺寸超过400x400的限制
        if(originWidth > maxWidth || originHeight > maxHeight) {
            if(originWidth / originHeight > maxWidth / maxHeight) {
                // 更宽，按照宽度限定尺寸
                targetWidth = maxWidth;
                targetHeight = Math.round(maxWidth * (originHeight / originWidth));
            } else {
                targetHeight = maxHeight;
                targetWidth = Math.round(maxHeight * (originWidth / originHeight));
            }
        }
        // canvas对图片进行缩放
        canvas.width = targetWidth;
        canvas.height = targetHeight;
        transformCoordinate(canvas, targetWidth, targetHeight, Orientation);
        // 图片压缩
        var ctx = canvas.getContext("2d"); 
        ctx.clearRect(0, 0, targetWidth, targetHeight);
        ctx.drawImage(image, 0, 0, targetWidth, targetHeight);
        /*第一个参数是创建的img对象；第二个参数是左上角坐标，后面两个是画布区域宽高*/
        // ctx.drawImage(that, 0, 0, w, h); 
        var base64 = null; 
        base64 = canvas.toDataURL("image/jpeg", 0.7); 
        request_uploadImg(base64, do_success_uploadimg, do_failed_uploadimg);
      }; 
    }; 
    oReader.readAsDataURL(file); 
  } 
}

function upload_img_obj(fileObj, do_success_uploadimg, do_failed_uploadimg, func_complete) { 
  var file = fileObj; 
  { 
    // var URL = URL || webkitURL; 
    //获取照片方向角属性，用户旋转控制 
    EXIF.getData(file, function() { 
      // alert(EXIF.pretty(this)); 
      EXIF.getAllTags(this);  
      //alert(EXIF.getTag(this, 'Orientation'));  
      Orientation = EXIF.getTag(this, 'Orientation'); 
      //return; 
    }); 
      
    var oReader = new FileReader(); 
    oReader.onload = function(e) { 
      //var blob = URL.createObjectURL(file); 
      //_compress(blob, file, basePath);

      var URL = window.URL && window.URL.createObjectURL ? window.URL : window.webkitURL && window.webkitURL.createObjectURL ? window.webkitURL : null;
      var src = URL.createObjectURL(file);

      var image = new Image(); 
      image.src = src;//e.target.result; 
      image.onload = function() { 
        var that = this;
        var canvas = document.createElement("canvas"); 
        // 图片原始尺寸
        var originWidth = this.width;
        var originHeight = this.height;
        // 最大尺寸限制，可通过国设置宽高来实现图片压缩程度
        var maxWidth = 800,
            maxHeight = 800;
        // 目标尺寸
        var targetWidth = originWidth,
            targetHeight = originHeight;
        // 图片尺寸超过400x400的限制
        if(originWidth > maxWidth || originHeight > maxHeight) {
            if(originWidth / originHeight > maxWidth / maxHeight) {
                // 更宽，按照宽度限定尺寸
                targetWidth = maxWidth;
                targetHeight = Math.round(maxWidth * (originHeight / originWidth));
            } else {
                targetHeight = maxHeight;
                targetWidth = Math.round(maxHeight * (originWidth / originHeight));
            }
        }
        // canvas对图片进行缩放
        canvas.width = targetWidth;
        canvas.height = targetHeight;
        transformCoordinate(canvas, targetWidth, targetHeight, Orientation);
        // 图片压缩
        var ctx = canvas.getContext("2d"); 
        ctx.clearRect(0, 0, targetWidth, targetHeight);
        ctx.drawImage(image, 0, 0, targetWidth, targetHeight);
        /*第一个参数是创建的img对象；第二个参数是左上角坐标，后面两个是画布区域宽高*/
        // ctx.drawImage(that, 0, 0, w, h); 
        var base64 = null; 
        base64 = canvas.toDataURL("image/jpeg", 0.7); 
        request_uploadImg(base64, do_success_uploadimg, do_failed_uploadimg, func_complete);
      }; 
    }; 
    oReader.readAsDataURL(file); 
  } 
}


function upload_video_obj(fileObj, do_success_uploadimg, do_failed_uploadimg, func_complete){
  var file = fileObj; 
  var formdata = new FormData(file);
  var param = {};

  // debug
  // $.each(($("#upload-form input")), function(i,n) {
  //   var id = $(n).attr("id");
  //   param[i] = {
  //     id:id,
  //     lastModified:n.files[0].lastModified
  //   };
  // });
  
  $.ajax({
      url:_common.config.apiUrl+'file/file/index',
      type:'POST',
      data:formdata,
      async: true,  
      cache: false, 
      timeout:"30000",
      contentType: false, //不设置内容类型
      processData: false, //不处理数据
      success:function(data){
        if(success != null){
          success(data,param);
        }
      },
      error:function(){
        if(error != null){
          error({
            code:-10000,
            msg:"网络请求失败"
          },param);
        }
      }
    })
}


function get_scale_img(fileObj, config, func_success) { 
  var file = fileObj.files[0]; 
  var height = config.height;

  //图片方向角 added by lzk 
  var Orientation = null; 
    
  if (file) { 
    var rFilter = /^(image\/jpeg|image\/png)$/i; // 检查图片格式 
    if (!rFilter.test(file.type)) { 
      //showMyTips("请选择jpeg、png格式的图片", false); 
      return; 
    } 
    // var URL = URL || webkitURL; 
    //获取照片方向角属性，用户旋转控制 
    EXIF.getData(file, function() { 
      // alert(EXIF.pretty(this)); 
      EXIF.getAllTags(this);  
      //alert(EXIF.getTag(this, 'Orientation'));  
      Orientation = EXIF.getTag(this, 'Orientation'); 
      //return; 
    }); 
      
    var oReader = new FileReader(); 
    oReader.onload = function(e) { 

      var URL = window.URL && window.URL.createObjectURL ? window.URL : window.webkitURL && window.webkitURL.createObjectURL ? window.webkitURL : null;
      var src = URL.createObjectURL(file);

      var image = new Image(); 
      image.src = src;//e.target.result; 
      image.onload = function() { 
        var that = this;
        var canvas = document.createElement("canvas"); 
        // 图片原始尺寸
        var originWidth = this.width;
        var originHeight = this.height;
        // 最大尺寸限制，可通过国设置宽高来实现图片压缩程度
        var maxWidth = 800,
            maxHeight = height;
        // 目标尺寸
        var targetWidth = width,
            targetHeight = height;
        // 图片尺寸超过400x400的限制
        if(originWidth > maxWidth || originHeight > maxHeight) {
            if(originWidth / originHeight > maxWidth / maxHeight) {
                // 更宽，按照宽度限定尺寸
                targetWidth = maxWidth;
                targetHeight = Math.round(maxWidth * (originHeight / originWidth));
            } else {
                targetHeight = maxHeight;
                targetWidth = Math.round(maxHeight * (originWidth / originHeight));
            }
        }
        // canvas对图片进行缩放
        canvas.width = targetWidth;
        canvas.height = targetHeight;
        transformCoordinate(canvas, targetWidth, targetHeight, Orientation);
        // 图片压缩
        var ctx = canvas.getContext("2d"); 
        ctx.clearRect(0, 0, targetWidth, targetHeight);
        ctx.drawImage(image, 0, 0, targetWidth, targetHeight);
        /*第一个参数是创建的img对象；第二个参数是左上角坐标，后面两个是画布区域宽高*/
        // ctx.drawImage(that, 0, 0, w, h); 
        var base64 = null; 
        base64 = canvas.toDataURL("image/jpeg", 0.7); 

        func_success(base64);
      }; 
    }; 
    oReader.readAsDataURL(file); 
  } 
}


function request_uploadImg(str_base64_img, do_success_uploadimg, do_failed_uploadimg, func_complete){
  console.log("====");
  console.log(str_base64_img);
  // var list_imgs = new Array();
  // list_imgs.push(str_base64_img.toString());

  // var post_config = {
  // "url":fg_getAppApiOnlyCn("/File/uploadFileString"),
  // "data":do_getJSONStr(list_imgs),
  // "func_before": null,
  // "func_success": do_success_uploadimg,
  // "func_complete": null,
  // "func_error":do_handlerErrorRequest };
  // request_api_b(post_config);

  do_success_uploadimg()
  func_complete()
}


function preview_uploadimg(t, str_target) {
  var objUrl = getObjectURL(t.files[0]) //获取图片的路径，该路径不是图片在本地的路径
    if (objUrl) {
        $(str_target).attr("src", objUrl) //将图片路径存入src中，显示出图片
    }
}
//建立一個可存取到該file的url
function getObjectURL(file) {
    var url = null ;
    if (window.createObjectURL!=undefined) { // basic
    url = window.createObjectURL(file) ;
    } else if (window.URL!=undefined) { // mozilla(firefox)
    url = window.URL.createObjectURL(file) ;
    } else if (window.webkitURL!=undefined) { // webkit or chrome
    url = window.webkitURL.createObjectURL(file) ;
    }
    return url ;
}

//获取图片方向
function getPhotoOrientation(img) {
   var orient;
   EXIF.getData(img, function () {
      orient = EXIF.getTag(this, 'Orientation');
   });
   return orient;
}

//图片压缩
function compress(img, width, height, ratio) {
   var canvas, ctx, img64, orient;
　　　 
   //获取图片方向
   orient = getPhotoOrientation(img);
 
   canvas = document.createElement('canvas');
   canvas.width = width;
   canvas.height = height;
 
   ctx = canvas.getContext("2d");
 
   //如果图片方向等于6 ，则旋转矫正，反之则不做处理
   if (orient == 6) {
      ctx.save();
      ctx.translate(width / 2, height / 2);
      ctx.rotate(90 * Math.PI / 180);
      ctx.drawImage(img, 0 - height / 2, 0 - width / 2, height, width);
      ctx.restore();
   } else {
      ctx.drawImage(img, 0, 0, width, height);
   }
 
   img64 = canvas.toDataURL("image/jpeg", ratio);
   return img64;
}

function AutoResizeImage(maxWidth,maxHeight,objImg){
    var img = new Image();
    img.src = objImg.src;
    var hRatio;
    var wRatio;
    var Ratio = 1;
    var w = img.width;
    var h = img.height;
    wRatio = maxWidth / w;
    hRatio = maxHeight / h;
    if (maxWidth ==0 && maxHeight==0){
    Ratio = 1;
    }else if (maxWidth==0){//
    if (hRatio<1) Ratio = hRatio;
    }else if (maxHeight==0){
    if (wRatio<1) Ratio = wRatio;
    }else if (wRatio<1 || hRatio<1){
    Ratio = (wRatio<=hRatio?wRatio:hRatio);
    }
    if (Ratio<1){
    w = w * Ratio;
    h = h * Ratio;
    }
    objImg.height = h;
    objImg.width = w;
}

function orientation(orientation) {
    var o = 0;

    switch (orientation) {
        case "left-bottom":
            o = 8;
            break;
        case "right-bottom":
            o = 7;
            break;
        case "right-top":
            o = 6;
            break;
        case "left-top":
            o = 5;
            break;
        case "bottom-left":
            o = 4;
            break;
        case "bottom-right":
            o = 3;
            break;
        case "top-right":
            o = 2;
            break;
        default:
            o = 0;
    }

    return o;
}


function transformCoordinate(canvas, width, height, orientation) {
    //console.log(orientation);
    if (!orientation) {
        return;
    }
    canvas.width = width;
    canvas.height = height;
    if (orientation > 4) {
        canvas.width = height;
        canvas.height = width;
    }
    var ctx = canvas.getContext('2d');
    switch (orientation) {
        case 2:
            // horizontal flip
            ctx.translate(width, 0);
            ctx.scale(-1, 1);
            break;
        case 3:
            // 180° rotate left
            ctx.translate(width, height);
            ctx.rotate(Math.PI);
            break;
        case 4:
            // vertical flip
            ctx.translate(0, height);
            ctx.scale(1, -1);
            break;
        case 5:
            // vertical flip + 90 rotate right
            ctx.rotate(0.5 * Math.PI);
            ctx.scale(1, -1);
            break;
        case 6:
            // 90° rotate right
            ctx.rotate(0.5 * Math.PI);
            ctx.translate(0, -height);
            break;
        case 7:
            // horizontal flip + 90 rotate right
            ctx.rotate(0.5 * Math.PI);
            ctx.translate(width, -height);
            ctx.scale(-1, 1);
            break;
        case 8:
            // 90° rotate left
            ctx.rotate(-0.5 * Math.PI);
            ctx.translate(-width, 0);
            break;
    }
}