import db
import socketserver

class rdpServer():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serverADDR = ('localhost', 33893)
    sock.bind(serverADDR)

    sock.listen(1)

    while True:
        # Wait for a connection
        print >>sys.stderr, 'waiting for a connection'
        connection, client_address = sock.accept()
            try:
            print >>sys.stderr, 'connection from', client_address

            # Receive the data in small chunks and retransmit it
            while True:
                data = connection.recv(16)
                print >>sys.stderr, 'received "%s"' % data
                if data:
                    print >>sys.stderr, 'sending data back to the client'
                    connection.sendall(data)
                else:
                    print >>sys.stderr, 'no more data from', client_address
                    break
            
            finally:
                # Clean up the connection
                connection.close()




### Test connaction block ###