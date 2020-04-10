import email
import matplotlib.pyplot as plt
import numpy as np
import wave
import sys

msg = email.message_from_file(open("message.eml"))

attachments=msg.get_payload()

for attachment in attachments:
    try:
        fnam=attachment.get_filename()
        f=open(fnam, 'wb').write(attachment.get_payload(decode=True,))
        f.close()
    except Exception as detail:
        pass




spf = wave.open("indian.wav", "r")

# Extract Raw Audio from Wav File
signal = spf.readframes(-1)
signal = np.fromstring(signal, "Int16")


# If Stereo
if spf.getnchannels() == 2:
    print("Just mono files")
    sys.exit(0)

plt.figure(1)
plt.title("Signal Wave...")
plt.plot(signal)
plt.show()
