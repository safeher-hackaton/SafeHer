import speech_recognition as sr


class UnknownMic(Exception):
    """Raised when the mic is unknown"""
    pass


class UnableToParse(Exception):
    """Raised when the unable to parse"""
    pass


class AudioAI:
    def __init__(self):
        self.__recognizer = sr.Recognizer()
        self.__mic_index = None
        self.__mic = None

    def __int__(self, mic_index=None, mic_name=None):
        self.__recognizer = sr.Recognizer()
        self.__mic = None
        self.__mic_index = mic_index
        if self.__mic_index is not None:
            self.initialize_mic()
        elif mic_name is not None:
            self.choose_mic(mic_name=mic_name)

    def initialize_mic(self, index: int):
        self.__mic = sr.Microphone(device_index=index)
        with self.__mic as source:
            self.__recognizer.adjust_for_ambient_noise(source, duration=4)

    @staticmethod
    def get_mics() -> list:
        return sr.Microphone.list_microphone_names()

    def choose_mic(self, mic_index=None, mic_name=None):
        mic_list = sr.Microphone.list_microphone_names()
        if mic_index is not None:
            if mic_index in range(len(mic_list)):
                self.__mic_index = mic_index
                self.initialize_mic()
                return
            else:
                raise UnknownMic
        if mic_name in sr.Microphone.list_microphone_names():
            for i in range(len(mic_list)):
                if str(mic_list[i]) == mic_name:
                    self.__mic_index = i
                    self.initialize_mic()
                    return
            raise UnknownMic

    def recognize_audio_stream(self, filename: str) -> str:
        r = self.__recognizer
        audio_file = sr.AudioFile(filename)
        with audio_file as source:
            audio = r.record(source)
            try:
                return r.recognize_google(audio)
            except sr.UnknownValueError:
                raise UnableToParse
        return ""

    def recognize_audio_mic(self) -> str:
        r = self.__recognizer
        if self.__mic is not None:
            mic = self.__mic
        elif self.__mic_index is not None:
            mic = sr.Microphone(device_index=self.__mic_index)
        else:
            raise UnknownMic
        with mic as source:
            audio = r.listen(source)
            try:
                return r.recognize_google(audio)
            except sr.UnknownValueError:
                raise UnableToParse
