import configparser
import time
from signal_finders import youtube_finder, key_actor_finder, sentiment_finder, anomaly_finder

def load_config():
    """Loads user config from config.ini."""
    print("Loading configuration from config.ini...")
    config = configparser.ConfigParser()
    try:
        config.read('config.ini')
        if 'API_KEYS' not in config:
            raise FileNotFoundError
    except FileNotFoundError:
        print("="*50)
        print("ERROR: 'config.ini' not found.")
        print("Please copy 'config.ini.example' to 'config.ini'")
        print("and add your API keys to use the BYOK model.")
        print("="*50)
        return None
    
    return config

def run_signal_scan(config):
    """Main scan loop for finding signals."""
    print("\n" + "="*20 + " [Starting New Scan Cycle] " + "="*20)
    
    # --- Run each "Signal Finder" module ---
    
    # 1. YouTube Distillation (Section 3.1)
    print("\n[Module] Running 'Long-Form Content Distiller' (YouTube)...")
    youtube_signals = youtube_finder.scan(config)
    for signal in youtube_signals:
        print(f"  -> New YouTube Signal: {signal['signal']}")

    # 2. Key Actor Detection (Section 3.1)
    print("\n[Module] Running 'Key Actor' Detector (On-Chain/Social)...")
    actor_signals = key_actor_finder.scan(config)
    for signal in actor_signals:
        print(f"  -> New Key Actor Signal: {signal['signal']}")

    # 3. Anomaly Detection (Section 3.1)
    print("\n[Module] Running 'New Data Anomaly' Detector (SEC/Patents)...")
    anomaly_signals = anomaly_finder.scan(config)
    for signal in anomaly_signals:
        print(f"  -> New Anomaly Signal: {signal['signal']}")

    # 4. Sentiment Analysis (Section 3.1)
    print("\n[Module] Running 'Sentiment & Hype' Analyzer (Twitter/Reddit)...")
    sentiment_signals = sentiment_finder.scan(config)
    for signal in sentiment_signals:
        print(f"  -> New Sentiment Signal: {signal['signal']}")
    
    print("\n" + "="*20 + " [Scan Cycle Complete] " + "="*23)

def main():
    """Main entry point for Project Signal."""
    print("--- Welcome to Project Signal (Prototype V1.0) ---")
    print("This prototype simulates the 'Signal-Finder' AI Engine.")
    
    config = load_config()
    
    if config:
        interval_min = config.getint('SETTINGS', 'SCAN_INTERVAL_MINUTES', fallback=60)
        print(f"\nConfiguration loaded. Scan interval set to {interval_min} minutes.")
        
        try:
            while True:
                run_signal_scan(config)
                print(f"Sleeping for {interval_min} minutes... (Press Ctrl+C to stop)")
                time.sleep(interval_min * 60)
        except KeyboardInterrupt:
            print("\nShutdown signal received. Exiting Project Signal.")

if __name__ == "__main__":
    main()