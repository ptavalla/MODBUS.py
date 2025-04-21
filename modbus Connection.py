import socket

O3D_IP = "192.168.0.69"
MODBUS_PORT = 1024

MODBUS_REQUEST = bytes([0x00, 0x01,
                       0x00, 0x00,
                       0x00, 0x06,
                       0x01,
                       0x03,
                       0x00, 0x64,
                       0x00, 0x0A])
try:
    print("creating a socket")
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.settimeout(2)
    
    print(f"Connecting to {O3D_IP}:{MODBUS_PORT}...")
    client.connect((O3D_IP, MODBUS_PORT))
    print("Successfully connected to O3D300 Modbus TCP!")
    
    print ("Sending Modbus request...")
    client.send(MODBUS_REQUEST)
    print("Receiving Response...")
    
    response = client.recv(1024)
    
    print ("Response Type:", type(response))
    print ("Raw Modbus Response(hex):". response.hex())
    
    
   # if isinstance(response, bytes):
        
    
    #    data = response[9:]
    
#    for i in range(0, len(data), 2):
 #       value = int.from_bytes(data[i:i+2], byteorder='big')
  #      print(f"Register{i//2}: {value}")
   # else:
    #    print ("Error: Received response is not in bytes format.")
    
    
    client.close()
    print ("Connection Closed.")
except AttributeError as attr_err:
    print(f"AttributeError:{attr_err}")

except Exception as e:
        print (f"General Error: {e}")