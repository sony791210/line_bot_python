* 1.python 基本的  
- 2.nginx 後臺控制  
- 3.uwgis 連接python 與 nginx 之間的溝通  
* 4.dehydrated 處理ssl 的問題,因為linebot 需要https的服務才能  




# python install
    anaconda install .....please google  
    安裝flask  
    執行第一個案例  
    python 1_flask_hellow/hellow.py  
    在網頁中打開　127.0.0.1:5000   

# nginx 及uwsgi  install
參考 ref:https://stackoverflow.com/questions/24912827/nginx-error-unknown-directive-uwsgi-param  
    sudo apt-get install nginx  
    sudo apt-get install uwsgi  
    sudo apt-get install uwsgi-plugin-python  
    conda install -c conda-forge uwsgi
    conda install -c conda-forge libiconv 



# nginx 及uwsgi 設定
ref:http://blog.changyy.org/2018/06/python-line-chatbot-echo-service-ubuntu.html  
## uwsgi 相關設定
    2_flask_uwgis 相關設定
    sudo vi /etc/systemd/system/chatbot.uwsgi.service  
    配合myproject.ini的設定使用  
    相關錯誤訊息請看 裡面有相關資訊  
    ls /var/log/uwsgi/  

## nginx 的安裝路徑 相關資訊放github nginx資料夾 裡面
    sudo vi /etc/nginx/sites-available/default  
    修改裡面的資訊後重啟服務  
    service nginx restart  
    相關錯誤訊息請看 裡面有相關資訊  
    sudo vi /var/log/nginx/error.log  


# dehydrated  
Let’s Encrypt   SSL 申請    

Ref: https://wiki.gslin.org/wiki/Dehydrated  
Ref: https://blog.wu-boy.com/2016/10/website-support-http2-using-letsencrypt/  

## 安裝
    sudo add-apt-repository ppa:gslin/dehydrated-lite  
    sudo apt update  
    sudo apt install dehydrated-lite  
## 基本設定  
    echo "WELLKNOWN=/var/www/dehydrated" > /etc/dehydrated/config  
    sudo mkdir /etc/dehydrated  
    sudo touch /etc/dehydrated/config 
    sudo mkdir /var/www/dehydrated
## 安裝 dehydrated
    cd  /etc/dehydrated/
    wget https://raw.githubusercontent.com/lukas2511/dehydrated/master/dehydrated -O /
    chmod 755 /etc/dehydrated/dehydrated
## 設定nginx的conf ，在80port
    location /.well-known/acme-challenge/ {
        alias /var/www/dehydrated/;
    }
## 域名設定  “blog.gslin.org” 換成你的網域名稱 如DDNS
    cd /etc/dehydrated
    echo  'blog.gslin.org' | sudo tee -a domains.txt
##  第一次需要同意條款
    sudo dehydrated --register --accept-terms  
##  驗證憑證，fbbot.wu-boy.com代表你的網域
    /etc/dehydrated/dehydrated -c -d fbbot.wu-boy.com


# line
官方的
Ref: https://github.com/line/line-bot-sdk-python#imagesendmessage
參考這位寫的真的很強了
Ref: https://github.com/twtrubiks/line-bot-tutorial
Ref: https://github.com/twtrubiks/line-bot-imgur-tutorial


