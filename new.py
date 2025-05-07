from TTS.utils.manage import ModelManager
from TTS.utils.synthesizer import Synthesizer
import tempfile

# Define paths
MODEL_PATH = "models/hindi_vakyansh/model.pth"
CONFIG_PATH = "models/hindi_vakyansh/config.json"

# Optional: vocoder (or use Griffin-Lim fallback)
VOCODER_PATH = None
VOCODER_CONFIG_PATH = None

# Load synthesizer
synthesizer = Synthesizer(
    tts_checkpoint=MODEL_PATH,
    tts_config_path=CONFIG_PATH,
    vocoder_checkpoint=VOCODER_PATH,
    vocoder_config=VOCODER_CONFIG_PATH,
    use_cuda=False
)

# Generate audio
text = "यह एक परीक्षण वाक्य है"
with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as f:
    synthesizer.save_wav(text, f.name)
    print("✅ Audio saved at:", f.name)