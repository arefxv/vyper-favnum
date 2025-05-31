import boa
from dotenv import load_dotenv
from boa.network import NetworkEnv, EthereumRPC
import os
from eth_account import Account

load_dotenv()

def main():
    rpc = os.getenv("RPC_URL")
    env = NetworkEnv(EthereumRPC(rpc))
    boa.set_env(env)

    anvil_key = os.getenv("ANVIL_KEY")
    my_account = Account.from_key(anvil_key)
    boa.env.add_account(my_account, force_eoa=True)

    favorites_contract = boa.load("favorites.vy")

    starting_favorite_number = favorites_contract.retrieve()
    print(f"Starting favorite number is {starting_favorite_number}")

    print("Storing number...")
    favorites_contract.store(5)

    ending_favorite_number = favorites_contract.retrieve()
    print(f"Ending favorite number is {ending_favorite_number}")

if __name__ == "__main__":
    main()