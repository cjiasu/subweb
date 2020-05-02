#全局变量定义
aff = 'C加速官方接口,禁止调用！'   
subip = 'http://172.104.114.82:10010'      #默认apiip 是web的端口，在api.py的main函数指定，或者docker的端口指定。  默认subip是 subconverter 的端口，在config/perf.ini 中指定，或者docker的端口指定。
apiip = 'http://172.104.114.82'          #套CDN后，可以在服务器上整反代，将域名反代到本地运行的端口：http://127.0.0.1:10010 
