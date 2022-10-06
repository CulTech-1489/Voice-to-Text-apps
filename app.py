# import io
# import os
from google.cloud import speech
import streamlit as st


# os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'secret.json'

def file_translation(speech_file, lang='日本語'):

    lang_code = {
        '英語':'en-US',
        '日本語':'ja-JP',
        '中国語':'zh'
        }
        
    client = speech.SpeechClient()
        
#    with io.open(speech_file, 'rb') as f:
#       content = f.read()
        
    audio = speech.RecognitionAudio(content = content)

    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.ENCODING_UNSPECIFIED,
        sample_rate_hertz=16000,
        language_code=lang_code[lang],
    )

    response = client.recognize(config=config, audio=audio)

    for result in response.results:
        st.write(result.alternatives[0].transcript)
        #print(result)
#        print("認識結果: {}".format(result.alternatives[0].transcript))
        
st.title('音声をテキストに！！')
st.header('General')
st.write('Google Cloud[Speech to Text]を使ったアプリケーションです。詳細は下記リンクから。')
st.markdown('<a href="https://cloud.google.com/speech-to-text?hl=ja">Speech to Text</a>' , unsafe_allow_html=True)

upload_file = st.file_uploader('ファイルをアップロードしてください' , type=['mp3','wav'])
if upload_file is not None:
    content = upload_file.read()
    st.subheader('ファイル詳細')
    file_details = {'Filename': upload_file.name, 'Filetype': upload_file.type, 'Filesize':upload_file.size}
    st.write(file_details)
    st.subheader('音声の再生')
    st.audio(content)
    
    st.subheader('言語選択')
    option = st.selectbox('言語選択をしてください', ('英語','日本語','中国語'))
    st.write('選択言語:', option)
    
    st.write('文字起こし')
    if st.button('START'):
        comment = st.empty()
        comment.write('writing now ...')
        file_translation(content , lang=option)
        comment.write('Completed.')
        
        
        
