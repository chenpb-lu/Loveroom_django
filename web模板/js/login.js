$(function(){


	// 文本框获得焦点
	$(".mainForm input").focus(function(){
		$("#mz_Float_login").css("display","block");
	});


	//mainform1


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
	$(".password,.password1").focus(function(){
		$(".password").parent().removeClass("errorC");
		$(this).parent().removeClass("checkedN");
		$(".error3").hide();
		if($(".error1").css("display")=="block" && $(".error2").css("display")=="block")
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


	//mainform1end



	//mainForm2

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


});

