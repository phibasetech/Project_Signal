from .base_finder import BaseFinder

class AnomalyFinder(BaseFinder):
    """
    Implements 'New Data Anomaly' Detection for SEC/Legal filings.
    """
    def __init__(self):
        super().__init__("AnomalyFinder")

    def scan(self, config):
        api_key = config.get('API_KEYS', 'SEC_API_KEY')
        if not api_key or api_key == "Your_Key_Here":
            self._log("SEC API key not set. Skipping.")
            return []

        self._log("Scanning for SEC filing anomalies... (Prototype, no real API call)")

        # --- PROTOTYPE: Return a fake signal from Whitepaper Scenario 2 ---
        fake_signal = {
            "source": "SEC Filing",
            "signal": "Contradiction detected. Press release claims 50% growth, but new 10-K filing (page 82, clause 2.a) attributes 40% to one-time accounting change.",
            "url": "https://sec.gov/example"
        }
        return [fake_signal]

# Create a single instance
scan = AnomalyFinder().scan