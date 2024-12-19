from flask import Flask, render_template, request
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)

# Yüklenen dosyaların kaydedileceği klasör
UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Dosya uzantıları kontrolü
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

# Dosya uzantısı kontrolü fonksiyonu
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Dosya yükleme işlemi
        file = request.files.get('image')  # 'image' form elemanından dosya alıyoruz
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)

            # static/uploads/ klasörünü kontrol et, eğer yoksa oluştur
            if not os.path.exists(app.config['UPLOAD_FOLDER']):
                os.makedirs(app.config['UPLOAD_FOLDER'])

            # Dosyayı kaydet
            file.save(filepath)

            # Yüklenen resmin yolu
            image_url = os.path.join('uploads', filename)

            # Yüklenen resmin yolu ve başarılı işlem mesajı
            return render_template('index.html', image_url=image_url, message="The file has been uploaded successfully!")
        else:
            return render_template('index.html', message="Upload a valid file.")

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
