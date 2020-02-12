git clone https://github.com/nakata5321/Flask.git
cd Flask
docker build -t <name_your_image> .
docker run -p 5000:5000 -d <name_your_image>
go to http://0.0.0.0:5000/
