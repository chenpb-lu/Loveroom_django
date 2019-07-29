$(function(){
	register_passwd_flag = false;
	register_kapkey_flag = false;
	register_phone_flag = false;
	phone_login_phone_flag = false;
	phone_login_kapkey_flag = false;
	pd_login_passwd_flag = false;
	pd_login_phone_flag = false;
	checkboxPic_flag = true;
	phone_login_checkboxPic_flag = true;
	pd_login_checkboxPic_flag = true;

	//页面切换初始化
	$(".number2").click(function(){
		$(".mainForm1").show();
		$(".mainForm2").hide();
		$(".error").hide();
		$(".normalInput").removeClass("errorC");
		$(".normalInput").removeClass("checkedN");
		$(".mainForm input").val("");
		$("#mz_Float").css("top","-10000px");
	});
	$(".number1").click(function(){
		$(".mainForm2").show();
		$(".mainForm1").hide();
		$(".error").hide();
		$(".normalInput").removeClass("errorC");
		$(".normalInput").removeClass("checkedN");
		$(".mainForm input").val("");
	});
	$(".register").click(function () {
		$(".mainForm1").show();
		$(".mainForm2").hide();
		$(".error").hide();
		$(".normalInput").removeClass("errorC");
		$(".normalInput").removeClass("checkedN");
		$(".mainForm input").val("");
		$("#mz_Float").css("top","-10000px");
    });
	// 注册
	//文本框失去焦点
	$(".mainForm input").blur(function(){
		$("#mz_Float").css("top","-10000px");
	});
	// 文本框获得焦点
	$(".mainForm input").focus(function(){
		$("#mz_Float").css("display","block");
	});

	// 协议条款
	$("#register_checkboxPic").click(function(){
		if($(this).attr("isshow")=="false")
		{
			$(this).parent().css("margin-bottom","10px");
			$("#register_checkboxPic i").css({"background-position":" -0px -127px"});
			$("#register_otherError").css("display","block");
			register_checkboxPic_flag = false;
			$(this).attr("isshow","true");
		}
		else
		{
			$(this).parent().css("margin-bottom","");
			$("#register_checkboxPic i").css({"background-position":"-31px -127px"});
			$("#register_otherError").hide();
			register_checkboxPic_flag = true;
			$(this).attr("isshow","false");
		}

	});


	//mainform1
	//密码是否可见(mainform1)
	$(".pwdBtnShow").click(function(){
		if($(".pwdBtnShow").attr("isshow")=="false")
		{
			$(".pwdBtnShow i").css("background-position","-30px -93px");
			$(".password").hide();
			$(".password1").val($(".password").val());
			$(".password1").show();
			$(".pwdBtnShow").attr("isshow","true");
		}
		else
		{
			$(".pwdBtnShow i").css("background-position","-60px -93px");
			$(".password1").hide();
			$(".password").val($(".password1").val());
			$(".password").show();
			$(".pwdBtnShow").attr("isshow","false");
		}

	});

	//手机号栏失去焦点
	$(".phone").blur(function(){
		reg=/^1[3|4|5|8][0-9]\d{4,8}$/i;//验证手机正则(输入前7位至11位)

		if( $(".phone").val()=="")
		{
			$(".phone").parent().addClass("errorC");
			$(".error1").html("请输入手机号");
			$(".error1").css("display","block");

		}
		else if($(".phone").val().length<11)
        {
        	$(".phone").parent().addClass("errorC");
            $(".error1").html("手机号长度有误！");
            $(".error1").css("display","block");

        }
        else if(!reg.test($(".phone").val()))
        {
        	$(".phone").parent().addClass("errorC");
            $(".error1").html("逗我呢吧，你确定这是你的手机号!!");
            $(".error1").css("display","block");

        }
        else
        {
        	$(".phone").parent().addClass("checkedN");
        	register_phone_flag = true;
        	phone_login_phone_flag = true;
        }
	});

	//验证码栏失去焦点
	$(".kapkey").blur(function(){
		reg=/^.*[\u4e00-\u9fa5]+.*$/;
		if( $(".kapkey").val()=="")
		{
			$(".kapkey").parent().addClass("errorC");
			$(".error2").html("请填写验证码");
			$(".error2").css("display","block");

		}
        else if($(".kapkey").val().length<6)
        {
        	$(".kapkey").parent().addClass("errorC");
            $(".error2").html("验证码长度有误！");
            $(".error2").css("display","block");

        }
        else if(reg.test($(".kapkey").val()))
        {
        	$(".kapkey").parent().addClass("errorC");
            $(".error2").html("验证码里无中文！");
            $(".error2").css("display","block");

        }
        else
        {
        	$(".kapkey").parent().addClass("checkedN");
        	register_kapkey_flag = true;
        	phone_login_kapkey_flag = true
        }
	});

	//密码栏失去焦点(mainform1)
	$(".password,.password1").blur(function(){
		reg1=/^.*[\d]+.*$/;
		reg2=/^.*[A-Za-z]+.*$/;
		reg3=/^.*[_@#%&^+-/*\/\\]+.*$/;//验证密码
		if($(".pwdBtnShow").attr("isshow")=="false")
		{
			var Pval = $(".password").val();
		}
		else
		{
			var Pval = $(".password1").val();
		}

		if( Pval =="")
		{
			$(".password").parent().addClass("errorC");
			$(".error3").html("请填写密码");
			$(".error3").css("display","block");

		}
        else if(Pval.length>16 || Pval.length<8)
        {
        	$(".password").parent().addClass("errorC");
            $(".error3").html("密码应为8-16个字符，区分大小写");
            $(".error3").css("display","block");

        }
        else if(!((reg1.test(Pval) && reg2.test(Pval)) || (reg1.test(Pval) && reg3.test(Pval)) || (reg2.test(Pval) && reg3.test(Pval)) ))
        {
        	$(".password").parent().addClass("errorC");
            $(".error3").html("需至少包含数字、字母和符号中的两种类型");
            $(".error3").css("display","block");

        }
        else
        {
        	$(".password").parent().addClass("checkedN");
        	register_passwd_flag = true;
        	pd_login_passwd_flag = true
        }
	});

	//手机号栏获得焦点
	$(".phone").focus(function(){
		$(".phone").parent().removeClass("errorC");
		$(".phone").parent().removeClass("checkedN");
		$(".error1").hide();
		$("#mz_Float").css("top","10px");
		$("#mz_Float").find(".bRadius2").html("输入11位手机号码，可用于登录和找回密码");
	});
	//验证码栏获得焦点
	$(".kapkey").focus(function(){
		$(".kapkey").parent().removeClass("errorC");
		$(".kapkey").parent().removeClass("checkedN");
		$(".error2").hide();
		if($(".error1").css("display")=="block")
		{
			$("#mz_Float").css("top","120px");
		}
		else
		{
			$("#mz_Float").css("top","90px");
		}

		$("#mz_Float").find(".bRadius2").html("请输入手机收到的验证码");
	});
	//密码栏获得焦点(mainform1)
	$(".password,.password1").focus(function(){
		$(".password").parent().removeClass("errorC");
		$(this).parent().removeClass("checkedN");
		$(".error3").hide();
		if($(".error1").css("display")=="block" && $(".error2").css("display")=="block")
		{
			$("#mz_Float").css("top","210px");
		}
		else if($(".error1").css("display")=="block" || $(".error2").css("display")=="block")
		{
			$("#mz_Float").css("top","190px");
		}
		else
		{
			$("#mz_Float").css("top","150px");
		}

		$("#mz_Float").find(".bRadius2").html("长度为8-16个字符，区分大小写，至少包含两种类型");
	});

// 登录
	$(".mainForm input").blur(function(){
		$("#mz_Float_login").css("top","-10000px");
	});
		// 文本框获得焦点
	$(".mainForm input").focus(function(){
		$("#mz_Float_login").css("display","block");
	});

	//mainform1

    $("#phone_login_checkboxPic").click(function(){
		if($(this).attr("isshow")=="false")
		{
			$(this).parent().css("margin-bottom","10px");
			$("#phone_login_checkboxPic i").css({"background-position":" -0px -127px"});
			$("#phone_login_otherError").css("display","block");
			phone_login_checkboxPic_flag = false;
			$(this).attr("isshow","true");
		}
		else
		{
			$(this).parent().css("margin-bottom","");
			$("#phone_login_checkboxPic i").css({"background-position":"-31px -127px"});
			$("#phone_login_otherError").hide();
			phone_login_checkboxPic_flag = true;
			$(this).attr("isshow","false");
		}

	});

	//密码是否可见(mainform1)
	$(".pwdBtnShowN").click(function(){
		if($(".pwdBtnShowN").attr("isshow")=="false")
		{
			$(".pwdBtnShowN i").css("background-position","-30px -93px");
			$(".passwordN").hide();
			$(".password1N").val($(".passwordN").val());
			$(".password1N").show();
			$(".pwdBtnShowN").attr("isshow","true");
		}
		else
		{
			$(".pwdBtnShowN i").css("background-position","-0px -93px");
			$(".password1N").hide();
			$(".passwordN").val($(".password1N").val());
			$(".passwordN").show();
			$(".pwdBtnShowN").attr("isshow","false");
		}

	});
	//手机号栏获得焦点
	$(".phone").focus(function(){
		$(".phone").parent().removeClass("errorC");
		$(".phone").parent().removeClass("checkedN");
		$(".error1").hide();
		$("#mz_Float_login").css("top","75px");
		$("#mz_Float_login").find(".bRadius2_login").html("输入11位手机号码，可用于登录和找回密码");
	});
	//验证码栏获得焦点
	$(".kapkey").focus(function(){
		$(".kapkey").parent().removeClass("errorC");
		$(".kapkey").parent().removeClass("checkedN");
		$(".error2").hide();
		if($(".error1").css("display")=="block")
		{
			$("#mz_Float_login").css("top","175px");
		}
		else
		{
			$("#mz_Float_login").css("top","145px");
		}

		$("#mz_Float_login").find(".bRadius2_login").html("请输入手机收到的验证码");
	});
	//密码栏获得焦点(mainform1)
	$(".passwordN,.password1N").focus(function(){
		$(".passwordN").parent().removeClass("errorC");
		$(this).parent().removeClass("checkedN");
		$(".error3").hide();
		if($(".error1").css("display")=="block" && $(".error2").css("display")=="block" )
		{
			$("#mz_Float_login").css("top","210px");
		}
		else if($(".error1").css("display")=="block" || $(".error2").css("display")=="block")
		{
			$("#mz_Float_login").css("top","190px");
		}
		else
		{
			$("#mz_Float_login").css("top","150px");
		}

		$("#mz_Float_login").find(".bRadius2_login").html("长度为8-16个字符，区分大小写，至少包含两种类型");
	});
	//密码栏失去焦点(mainform1)
	$(".passwordN,.password1N").blur(function(){
		reg1=/^.*[\d]+.*$/;
		reg2=/^.*[A-Za-z]+.*$/;
		reg3=/^.*[_@#%&^+-/*\/\\]+.*$/;//验证密码
		if($(".pwdBtnShowN").attr("isshow")=="false")
		{
			var Pval = $(".passwordN").val();
		}
		else
		{
			var Pval = $(".password1N").val();
		}

		if( Pval =="")
		{
			$(".passwordN").parent().addClass("errorC");
			$(".error3").html("请填写密码");
			$(".error3").css("display","block");

		}
        else if(Pval.length>16 || Pval.length<8)
        {
        	$(".passwordN").parent().addClass("errorC");
            $(".error3").html("密码应为8-16个字符，区分大小写");
            $(".error3").css("display","block");

        }
        else if(!((reg1.test(Pval) && reg2.test(Pval)) || (reg1.test(Pval) && reg3.test(Pval)) || (reg2.test(Pval) && reg3.test(Pval)) ))
        {
        	$(".passwordN").parent().addClass("errorC");
            $(".error3").html("需至少包含数字、字母和符号中的两种类型");
            $(".error3").css("display","block");

        }
        else
        {
        	$(".password").parent().addClass("checkedN");
        	register_passwd_flag = true;
        	pd_login_passwd_flag = true
        }
	});


	//mainform1end



	//mainForm2


      $("#pd_login_checkboxPic").click(function(){
		if($(this).attr("isshow")=="false")
		{
			$(this).parent().css("margin-bottom","10px");
			$("#pd_login_checkboxPic i").css({"background-position":" -0px -127px"});
			$("#pd_login_otherError").css("display","block");
			pd_login_checkboxPic_flag = false;
			$(this).attr("isshow","true");
		}
		else
		{
			$(this).parent().css("margin-bottom","");
			$("#pd_login_checkboxPic i").css({"background-position":"-31px -127px"});
			$("#pd_login_otherError").hide();
			pd_login_checkboxPic_flag = true;
			$(this).attr("isshow","false");
		}

	});

	//手机号获得焦点，用户名就是手机号
	$(".username").focus(function(){
		$(".username").parent().removeClass("errorC");
		$(".username").parent().removeClass("checkedN");
		$(".error1").hide();
		$("#mz_Float_login").css("top","75px");
		$("#mz_Float_login").find(".bRadius2_login").html("输入11位手机号码，可用于登录和找回密码");
	});

	//密码栏获得焦点(mainform2)
	$(".passwordN,.password1N").focus(function(){
		$(".passwordN").parent().removeClass("errorC");
		$(this).parent().removeClass("checkedN");
		$(".error3").hide();
		if($(".error1").css("display")=="block")
		{
			$("#mz_Float_login").css("top","190px");
		}
		else
		{
			$("#mz_Float_login").css("top","150px");
		}

		$("#mz_Float_login").find(".bRadius2_login").html("长度为8-16个字符，区分大小写，至少包含两种类型");
	});


	//手机号栏失去焦点
	$(".username").blur(function(){
		reg=/^1[3|4|5|8][0-9]\d{4,8}$/i;//验证手机正则(输入前7位至11位)

		if( $(".username").val()=="")
		{
			$(".username").parent().addClass("errorC");
			$(".error1").html("请输入手机号");
			$(".error1").css("display","block");

		}
		else if($(".username").val().length<11)
        {
        	$(".username").parent().addClass("errorC");
            $(".error1").html("手机号长度有误！");
            $(".error1").css("display","block");

        }
        else if(!reg.test($(".username").val()))
        {
        	$(".username").parent().addClass("errorC");
            $(".error1").html("逗我呢吧，你确定这是你的手机号!!");
            $(".error1").css("display","block");

        }
        else
        {
        	$(".username").parent().addClass("checkedN");
        	pd_login_phone_flag = true;
        }
	});



	 // 注册  判断是否可以提交数据
	 $("#register_flag").click(function () {

		if(register_kapkey_flag && register_passwd_flag && register_phone_flag && register_checkboxPic_flag)
		{
			alert("检查ok，提交表单");
    		$("#mainform1").submit()
		}else{
			alert("检查fail，提交表单");
		}
     });

	 	  // 密码  判断是否可以提交数据
	 $("#pw_login_flag").click(function () {
	 	console.log(111111);

		if(pd_login_passwd_flag && pd_login_phone_flag && pd_login_checkboxPic_flag)
		{
			alert("检查ok，提交表单");
    		$("#mainform2").submit()
		}else{
			alert("检查fail，提交表单");
		}
     });

	  // 手机验证码  判断是否可以提交数据
	 $("#phone_login_flag").click(function () {

		if(phone_login_phone_flag && phone_login_kapkey_flag && phone_login_checkboxPic_flag)
		{
			alert("检查ok，提交表单");
    		$("#mainform1").submit()
		}else{
			alert("检查fail，提交表单");
		}
     });




});

