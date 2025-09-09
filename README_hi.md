# शैक्षिक (Educational) View Simulation API

> **यह प्रोजेक्ट केवल शिक्षा के उद्देश्य से बनाया गया है।**
> यह किसी भी असली Instagram सेवा से कनेक्ट नहीं करता और
> किसी भी तरह से वास्तविक प्रोफाइल्स/व्यूज़ को प्रभावित नहीं करता।

यह एक छोटा API सर्वर है जो लोकल JSON फाइल में "IDs" और उनके "views" काउंटर को स्टोर करता है।
आप API endpoints को कॉल करके views को बढ़ा/घटा नहीं सकते — केवल बढ़ा सकते हैं — और लिस्ट देख सकते हैं।

## फ़ोल्डर स्ट्रक्चर
```
insta_view_sim/
├─ app/
│  ├─ main.py        # FastAPI endpoints
│  └─ storage.py     # ids.json लोड/सेव करने की utilities
├─ data/
│  └─ ids.json       # डमी IDs + views
├─ requirements.txt
└─ README_hi.md
```

## इंस्टॉलेशन और रन

### 1) वर्चुअल एन्वायरनमेंट (optional लेकिन सलाह दी जाती है)
```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
```

### 2) डिपेंडेंसीज़ इंस्टॉल करें
```bash
pip install -r requirements.txt
```

### 3) सर्वर चलाएँ
```bash
uvicorn app.main:app --reload --port 8000
```
अब ब्राउज़र में खोलें: `http://127.0.0.1:8000/docs` — यहाँ से आप सभी endpoints try कर सकते हैं।

## महत्वपूर्ण नोट
- यह **सिर्फ सिमुलेशन** है; किसी भी वास्तविक सोशल मीडिया प्लेटफॉर्म से कनेक्ट नहीं है।
- कृपया इसे किसी भी तरह की policy violation, स्पैमिंग या हानि पहुँचाने वाली गतिविधि के लिए न इस्तेमाल करें।

## Endpoints (संक्षेप में)
- `GET /health` — सर्वर स्टेटस
- `GET /ids` — वर्तमान IDs + views
- `POST /ids/add` — body: `{"ids": ["user1","user2"]}` — IDs जोड़ें
- `POST /view` — body: `{"id":"user1","increment":1}` — किसी एक ID के views बढ़ाएँ
- `POST /view/random` — मौजूद IDs में से किसी एक पर 1 view जोड़ें
- `GET /stats?limit=50` — सबसे ज़्यादा views वाले IDs देखें

## Pydroid 3 (Android) टिप्स
- `pip install -r requirements.txt` चलाएँ
- फिर `uvicorn app.main:app --port 8000` चलाएँ
- ब्राउज़र/इन-ऐप वेबव्यू में `http://127.0.0.1:8000/docs` खोलें