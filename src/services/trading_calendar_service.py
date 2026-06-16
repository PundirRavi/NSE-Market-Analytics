from datetime import datetime, time 

class TradingCalendarService:

    MARKET_OPEN = time(9,15)
    Market_ClOSE = time(15,30)

    def is_trading_day(self) -> bool:
        
        now = datetime.now()
        
        return now.weekday() < 5
    
    def is_market_hours(self) -> bool:

        current_time = datetime.now().time()

        return (
            self.MARKET_OPEN
            <= current_time
            <= self.Market_ClOSE
        )
    
    def is_market_open(self) -> bool:
        
        return(
            self.is_trading_day()
            and self.is_market_hours()
        )