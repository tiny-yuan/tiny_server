//  预加载
$(function () {
   // 轮播圆点
   var $carousel = $(".carousel-indicators");
   // 获取图片
    var $item = $(".carousel-inner .item");
    // 查看有没有获取到标签
    console.log($item.length);
    $carousel.delegate("li","click",function () {
        // 圆点的背景颜色变化
        $(this).addClass("active").siblings().removeClass("active");
        // 图片变化
        $item.eq($(this).index()).addClass("active").siblings().removeClass("active")
    });
//    轮播左右箭头
    // left边
  var $left =  $(".carousel-inner .left");
  $left.click(function () {
  //    现在图片所在的位置
      var $alt = $(".carousel-inner .active img").prop("alt");
      // console.log($alt)
  //     下一张图片
      if ($alt==="First slide"){
          $item.eq(2).addClass("active").siblings().removeClass("active");
          $carousel.children("li").eq(2).addClass("active").siblings().removeClass("active")
      }
      if ($alt==="Second slide"){
          $item.eq(0).addClass("active").siblings().removeClass("active");
          $carousel.children("li").eq(0).addClass("active").siblings().removeClass("active")
      }
      if ($alt==="Third slide"){
          $item.eq(1).addClass("active").siblings().removeClass("active");
          $carousel.children("li").eq(1).addClass("active").siblings().removeClass("active")
      }
  });
//    轮播左右箭头
    // right边
  var $right =  $(".carousel-inner .right");
  $right.click(function () {
  //    现在图片所在的位置
      var $alt = $(".carousel-inner .active img").prop("alt");
      // console.log($alt)
  //     下一张图片
      if ($alt==="First slide"){
          $item.eq(1).addClass("active").siblings().removeClass("active");
          $carousel.children("li").eq(1).addClass("active").siblings().removeClass("active")
      }
      if ($alt==="Second slide"){
          $item.eq(2).addClass("active").siblings().removeClass("active");
          $carousel.children("li").eq(2).addClass("active").siblings().removeClass("active")
      }
      if ($alt==="Third slide"){
          $item.eq(0).addClass("active").siblings().removeClass("active");
          $carousel.children("li").eq(0).addClass("active").siblings().removeClass("active")
      }
  });

//  题库类型
    var $dropdown = $("#dropdown");
    $dropdown.click(function () {
        var dropdown_menu = $("#dropdown-menu");
            dropdown_menu.toggle();
        dropdown_menu.delegate("li","click",function () {
            $dropdown.val($(this).text());
            dropdown_menu.hide();
        })
    });

//    选择题库
var listgroup = $("#list-group");
    listgroup.click(function () {
        $("#list-group-item").show();
        // 点击x消失
        $("#bank_id").click(function () {
            $("#list-group-item").hide()
        });
        // 点击使用题库，消失
        $("#list-group-btn").click(function () {
           var txt =  $("#tiku-name").children().eq(1).text()
            listgroup.text(txt);
           $("#list-group-item").hide()

        })
    });

//     登录页面点击退出
//     var $model = $("#model");
//     $("#close").click(function () {
//         $model.hide()
//     });


//    点击登录显示
    var $loginLabel = $("#login-label");
    // 登录事件
    $loginLabel.click(function () {
        $("#model").show();
        $("#signUpModel").hide();
        $("#resetPasswordModel").hide();

        // 点击提交按钮
        $("#signIn_btn").click(function () {
            // var $signInId = $("#signInId").val();
            // console.log($signInId);
            // console.log(checkEmail($signInId));
            if(!checkEmail( $("#signInId").val())){
                $("#signInId").val("");
                // attr(参数1，参数2)：或取并修改
                $("#signInId").attr("placeholder","邮箱格式错误！");
                $("#signInId").css("border","1px solid red")
            }else {
                $("#signInId").css("border","1px solid green")
            }
            return false
            // if(!checkEmail())

        });


        model_close($("#close"),$("#model"));
        // 注册页面
        $("#signUp").click(function () {
            $("#model").hide();
            $("#signUpModel").show();
            model_close($("#close-signUp"),$("#signUpModel"))
            $("#signIn").click(function () {
                $("#model").show();
                $("#signUpModel").hide()
            })
        });
        //  忘记密码
        $("#resetPassword").click(function () {
            $("#model").hide();
            $("#resetPasswordModel").show();
            model_close($("#close-reset"),$("#resetPasswordModel"));

        })

    });

//     退出函数
    function model_close(event1,event2) {

        event1.click(function () {
        console.log( event,"aaaaaaa");
        event2.hide()
        });
    }
//     邮箱函数检查
    function checkEmail(email) {
        // 1234sguf@qq.com.cn
        var re_rule = /^\w+@[\w\.]+\.[a-zA-Z]{2,5}$/;
        return re_rule.test(email)
    }
});