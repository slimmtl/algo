from algos.sma_algo import MovingAverageAlgo
from masterclasses import RiskModel, ExecutionModel, Account, BacktestModel
from settings import BACKTEST_CURRENCIES as BC


account = Account()
risk_model = RiskModel()
execution_model = ExecutionModel()
algorithm = MovingAverageAlgo(bc=BC)
backtest_model = BacktestModel(algorithm=algorithm)

backtest_model.visualize_backtest(BC[0])
