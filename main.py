from speedtest import Speedtest

st = Speedtest()
print('upload speed is ' + str(float(st.upload())/1000000) + ' Mbps')
print('download speed is ' + str(float(st.download())/1000000) + ' Mbps')
