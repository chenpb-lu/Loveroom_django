/**
 * Created by Administrator on 2019/7/29.
 */
$(function () {
    var ftit = '';
    var flink = '';
    var lk = '';
    //获取文章标题
    ftit = $('.pctitle').text();
    //获取网页中内容的第一张图片
    flink = $('.pcdetails img').eq(0).attr('src');
    if(typeof flink == 'undefined'){
        flink='';
    }
    //当内容中没有图片时，设置分享图片为网站logo
    if(flink == ''){
        lk = 'http://'+window.location.host+'/static/images/logo.png';
    }
    //如果是上传的图片则进行绝对路径拼接
    if(flink.indexOf('/uploads/') != -1) {
        lk = 'http://'+window.location.host+flink;
    }
    //qq空间接口的传参
    $(".qzone").click(function () {
        window.open('https://sns.qzone.qq.com/cgi-bin/qzshare/cgi_qzshare_onekey?url='+document.location.href+'?sharesource=qzone&title='+ftit+'&pics='+lk+'&summary='+document.querySelector('meta[name="description"]').getAttribute('content'));
    });

    //新浪微博接口的传参
    $(".weibo").click(function () {
        window.open('http://service.weibo.com/share/share.php?url='+document.location.href+'?sharesource=weibo&title='+ftit+'&pic='+lk+'&appkey=2706825840');
    });

    //qq好友接口的传参
    $(".qq").click(function () {
        window.open('http://connect.qq.com/widget/shareqq/index.html?url='+document.location.href+'?sharesource=qzone&title='+ftit+'&pics='+lk+'&summary='+document.querySelector('meta[name="description"]').getAttribute('content')+'&desc=php自学网，一个web开发交流的网站');
    });
    //生成二维码给微信扫描分享，php生成，也可以用jquery.qrcode.js插件实现二维码生成
    $(".wechat").click(function () {
        window.open('http://zixuephp.net/inc/qrcode_img.php?url=http://zixuephp.net/article-1.html');
    });

});