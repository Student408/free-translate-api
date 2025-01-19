import asyncio
import aiohttp
import pandas as pd
from datetime import datetime
import time

class KannadaTranslationTest:
    def __init__(self):
        self.endpoint = "http://localhost:8000/translate"
        self.test_sentences = [
            "ಅದಾನಿ ಸೇರಿದಂತೆ ಹಲವು ಕಾರ್ಪೋರೇಟ್ ದೈತ್ಯರ ಅಕ್ರಮಗಳನ್ನು ಬಯಲಿಗೆಳೆದಿದ್ದ ಅಮೆರಿಕದ ಶಾರ್ಟ್ ಸೆಲ್ಲರ್‌ ಸಂಸ್ಥೆ ಹಿಂಡನ್‌ಬರ್ಗ್‌ ರಿಸರ್ಚ್‌ ತನ್ನ ಕಾರ್ಯಾಚರಣೆ ಸ್ಥಗಿತಗೊಳಿಸಲು ನಿರ್ಧರಿಸಿದೆ."
            "ಅಮೆರಿಕ ಮೂಲದ ಸಣ್ಣ ಮಾರಾಟ ಘಟಕವಾಗಿರುವ ಹಿಂಡನ್ ಬರ್ಗ್​ ಅನ್ನು ವಿಸರ್ಜಿಸಲಾಗುತ್ತಿದ್ದು, ಈ ನಿರ್ಧಾರಕ್ಕೆ ನಿರ್ದಿಷ್ಟ ಕಾರಣ ಇಲ್ಲ."
            "ಯಾವುದೇ ಬೆದರಿಕೆ, ಯಾವುದೇ ಆರೋಗ್ಯ ಸಮಸ್ಯೆ ಮತ್ತು ಯಾವುದೇ ದೊಡ್ಡ ವೈಯಕ್ತಿಕ ಸಮಸ್ಯೆಯೂ ಇಲ್ಲ ಎಂದು ಸಂಸ್ಥಾಪಕ ನಾಟೆ ಆ್ಯಂಡರ್ಸನ್ ಘೋಷಿಸಿದ್ದಾರೆ."
            "ಸಂಸ್ಥೆ ಮುಚ್ಚುವ ಕುರಿತು ತಮ್ಮ ವೆಬ್​ಸೈಟ್​ನಲ್ಲಿ ಪೋಸ್ಟ್​ ಮಾಡಿರುವ ಆ್ಯಂಡರ್ಸನ್​, ಜಗತ್ತಿನಲ್ಲಿ ಅನೇಕ ವಿಚಾರಗಳನ್ನು ಹಾಗೂ ನಾನು ಕಾಳಜಿ ವಹಿಸುವ ವ್ಯಕ್ತಿಗಳನ್ನು ನಾನು ಮಿಸ್​ ಮಾಡಿಕೊಳ್ಳುತ್ತಿದ್ದೇನೆ."
            "ನನ್ನ ಜೀವನದಲ್ಲಿ ಹಿಂಡನ್​ ಬರ್ಗ್​​ ಅಧ್ಯಯನದ ಬಗ್ಗೆ ತಿಳಿದಿದೆ. ಆದರೆ, ಕೇಂದ್ರಿಕೃತ ವಿಚಾರಗಳು ಇವುಗಳನ್ನು ವ್ಯಾಖ್ಯಾನಿಸುವುದಿಲ್ಲ"
            "ನನ್ನ ಕುಟುಂಬ ಹಾಗೂ ತಂಡದೊಂದಿಗೆ ಕಳೆದ ವರ್ಷಾಂತ್ಯದಲ್ಲಿಯೇ ಈ ಕುರಿತು ನಾನು ಚರ್ಚಿಸಿದ್ದೆ."
            "ನಾನು ಯೋಚಿಸಿರುವ ಕೆಲವು ವಿಚಾರಗಳು ಒಂದು ಹಂತಕ್ಕೆ ಬಂದ ಮೇಲೆ ಇದನ್ನು ಮುಚ್ಚುವುದಕ್ಕೆ ನಿರ್ಧರಿಸಿದ್ದೆ."
            "ಅಂತಿಮ ವಿಚಾರಗಳು ಪೂರ್ಣಗೊಂಡಿದ್ದು, ನಿಯಾಮವಳಿಗಳಂತೆ ಇಂದು ಈ ಕುರಿತು ಮಾಹಿತಿ ಹಂಚಿಕೊಳ್ಳಲಾಗುತ್ತಿದೆ"
        ]
        self.results = []

    async def translate_text(self, session, text, index):
        start_time = time.time()
        try:
            async with session.post(
                self.endpoint,
                json={"text": text, "to": "en"},
                timeout=30
            ) as response:
                data = await response.json()
                response_time = time.time() - start_time
                self.results.append({
                    'chunk_number': index + 1,
                    'kannada_text': text,
                    'english_translation': data.get('translatedText', ''),
                    'status': response.status,
                    'response_time': f"{response_time:.2f}s"
                })
                print(f"Chunk {index + 1} translated in {response_time:.2f}s")
        except Exception as e:
            response_time = time.time() - start_time
            self.results.append({
                'chunk_number': index + 1,
                'kannada_text': text,
                'english_translation': '',
                'status': f'error: {str(e)}',
                'response_time': f"{response_time:.2f}s"
            })
            print(f"Error in chunk {index + 1}: {str(e)}")

    async def run_test(self, concurrent_requests=3):
        print(f"Starting translation test with {len(self.test_sentences)} chunks...")
        print(f"Processing {concurrent_requests} concurrent requests at a time")
        
        async with aiohttp.ClientSession() as session:
            for i in range(0, len(self.test_sentences), concurrent_requests):
                chunk = self.test_sentences[i:i + concurrent_requests]
                tasks = [
                    self.translate_text(session, text, idx + i) 
                    for idx, text in enumerate(chunk)
                ]
                await asyncio.gather(*tasks)
                await asyncio.sleep(1)  # Small delay between batches
        
        # Save results to CSV
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        df = pd.DataFrame(self.results)
        filename = f"kannada_translations_{timestamp}.csv"
        df.to_csv(filename, index=False, encoding='utf-8-sig')
        print(f"\nResults saved to {filename}")
        
        # Print summary
        success_count = sum(1 for r in self.results if str(r['status']).startswith('2'))
        print(f"\nSummary:")
        print(f"Total chunks: {len(self.test_sentences)}")
        print(f"Successful translations: {success_count}")
        print(f"Failed translations: {len(self.test_sentences) - success_count}")

async def main():
    tester = KannadaTranslationTest()
    await tester.run_test(concurrent_requests=3)  # Adjust concurrent requests here

if __name__ == "__main__":
    asyncio.run(main())