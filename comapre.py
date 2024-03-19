jhu = c.imread("jhuma.webp")
rgb_jhu = c.cvtColor(jhu, c.COLOR_BGR2RGB)
encode_jhu = face_recognition.face_encodings(rgb_jhu)[0]

prit = c.imread("pritam.webp")
rgb_prit = c.cvtColor(prit, c.COLOR_BGR2RGB)
encode_prit = face_recognition.face_encodings(rgb_prit)[0]

rau= c.imread("Raunak.webp")
rgb_rau= c.cvtColor(rau, c.COLOR_BGR2RGB)
encode_rau = face_recognition.face_encodings(rgb_rau)[0]

result = face_recognition.compare_faces([encode_rau], encode_prit)
print("result",result)

c.imshow("pritam",prit)
c.imshow("Jhuma",jhu)
c.imshow("Raunak",rau)
c.waitKey(0)
