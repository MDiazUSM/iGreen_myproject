import cv2  # Biblioteca para manejar imágenes y cámaras

def main():
   
    cap = cv2.VideoCapture(0) 
    
    detector = cv2.QRCodeDetector()

    

    while True:
       
        ret, frame = cap.read()

        if not ret:
            print("No se pudo acceder a la cámara.")
            break

        
        data, bbox, _ = detector.detectAndDecode(frame)

        if bbox is not None:
            
            for i in range(len(bbox)):
                point1 = tuple(map(int, bbox[i][0]))  
                point2 = tuple(map(int, bbox[(i + 1) % len(bbox)][0]))  
                cv2.line(frame, point1, point2, color=(0, 255, 0), thickness=2)

            
            if data:
                print(f"Código QR detectado: {data}")

        
        cv2.imshow("Lectura de QR", frame)

       
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
