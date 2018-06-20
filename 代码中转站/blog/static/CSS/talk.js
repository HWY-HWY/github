/**
 * Created by 沐宇宇 on 2018/6/16/016.
 */
window.onload = function () {
    var user = ["../img/img_17.jpg"];
    var num = 1;//判断左右
    var portrait_position = 0;
    var now = -1;//左右浮动
    var send_btn = document.getElementById('send_btn');
    var send_txt = document.getElementById('send_txt');
    var chat_ul = document.getElementById('chat_ul');
    var chat_span = chat_ul.getElementsByTagName('span');
    var chat_img = chat_ul.getElementsByTagName('img');
    send_btn.onclick = function () {
        if (send_txt.value == '') {
            alert("请不要惜字如金");
        } else {
            chat_ul.innerHTML += '<li><img src="../img/img_24.jpg"><span>' + send_txt.value + '</span>';
            now++;
            if (num==0) {
                chat_span[now].className = 'spanright';
                chat_img[now].className = 'imgright';
            }
             else {
                chat_span[now].className = 'spanleft';
                chat_img[now].className = 'imgleft';
            }
            send_txt.value = '';
            // 内容过多时,将滚动条放置到最底端
            /*contentcontent.scrollTop = content.scrollHeight;*/
        }
    }


}