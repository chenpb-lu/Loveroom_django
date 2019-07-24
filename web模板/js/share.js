/**
 * Created by Administrator on 2019/7/22.
 */
$(function () {
    console.log("xxxxx");
    $('.qq').click(shareTo);
    $('.qzone').click(shareTo);
    $('.weibo').click(shareTo);
    $('.wechat').click(shareTo);
    function shareTo(stype){
            // console.log(stype);
            // console.log(this.className);
            stype = this.className
            var ftit = '';
            var flink = '';
            var lk = '';
            //获取文章标题
            ftit = $('.pctitle').attr('content');
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
            //百度编辑器自带图片获取
            if(flink.indexOf('ueditor') != -1){
                lk = flink;
            }
            lk = "http://zixuephp.net/static/images/qqshare.png"
            //qq空间接口的传参
            if(stype=='qzone'){
//                window.open('https://sns.qzone.qq.com/cgi-bin/qzshare/cgi_qzshare_onekey?url=http://zixuephp.net/article-309.html?sharesource=qzone&title=一键分享到QQ空间、QQ好友、新浪微博、微信代码&pics=http://zixuephp.net/uploads/image/20170810/1502335815192079.png&summary=通过各自平台的开发接口，进行参数指定，进行一键分享javascript代码功能');
                url = 'https://sns.qzone.qq.com/cgi-bin/qzshare/cgi_qzshare_onekey?url=https://chenpb-lu.github.io&title='+ftit+'&pics='+lk+'&summary='+document.querySelector('meta[name="description"]').getAttribute('content')
                window.open(url);
            }
            //新浪微博接口的传参
            if(stype=='weibo'){
                window.open('http://service.weibo.com/share/share.php?url='+document.location.href+'&title='+ftit+'&pic='+lk+'&appkey=2706825840');
            }
            //qq好友接口的传参
            if(stype == 'qq'){
                window.open('http://connect.qq.com/widget/shareqq/index.html?url='+document.location.href+'?sharesource=qzone&title='+ftit+'&pics='+lk+'&summary='+document.querySelector('meta[name="description"]').getAttribute('content')+'&desc=php自学网，一个web开发交流的网站');
            }
            //生成二维码给微信扫描分享，php生成，也可以用jquery.qrcode.js插件实现二维码生成
            if(stype == 'wechat'){
                window.open('http://zixuephp.net/inc/qrcode_img.php?url=https://chenpb-lu.github.io');
            }
        }
})