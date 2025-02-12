# parameters and paths

# from sumo_env import SumoEnv
from anon_env import AnonEnv
from transfer_dqn_agent import TransferDQNAgent

DIC_EXP_CONF = {
    "RUN_COUNTS": 3600,
    "TEST_RUN_COUNTS": 3600,
    "TRAFFIC_FILE": [
        "cross.2phases_rou01_equal_450.xml"
    ],
    "MODEL_NAME": "SimpleDQN",
    "NUM_ROUNDS": 200,
    "NUM_GENERATORS": 3,
    "LIST_MODEL":
        ["TransferDQN"],
    "LIST_MODEL_NEED_TO_UPDATE":
        ["TransferDQN"],
    "MODEL_POOL": False,
    "NUM_BEST_MODEL": 3,
    "PRETRAIN": True,
    "PRETRAIN_MODEL_NAME": "Random",
    "PRETRAIN_NUM_ROUNDS": 10,
    "PRETRAIN_NUM_GENERATORS": 10,
    "AGGREGATE": False,
    "DEBUG": False,
    "EARLY_STOP": False,

    "MULTI_TRAFFIC": False,
    "MULTI_RANDOM": False,
}

dic_traffic_env_conf = {
    "ACTION_PATTERN": "set",
    "NUM_INTERSECTIONS": 1,
    "MIN_ACTION_TIME": 10,
    "YELLOW_TIME": 5,
    "ALL_RED_TIME": 0,
    "NUM_PHASES": 2,
    "NUM_LANES": 1,
    "ACTION_DIM": 2,
    "MEASURE_TIME": 10,
    "IF_GUI": True,
    "DEBUG": False,
    "BINARY_PHASE_EXPANSION": False,
    "DONE_ENABLE": False,

    "INTERVAL": 1,
    "THREADNUM": 1,
    "SAVEREPLAY": True,
    "RLTRAFFICLIGHT": True,

    "DIC_FEATURE_DIM": dict(
        D_LANE_QUEUE_LENGTH=(4,),
        D_LANE_NUM_VEHICLE=(4,),
        D_LANE_NUM_VEHICLE_BEEN_STOPPED_THRES1=(4,),
        D_CUR_PHASE=(1,),
        D_NEXT_PHASE=(1,),
        D_TIME_THIS_PHASE=(1,),
        D_TERMINAL=(1,),
        D_LANE_SUM_WAITING_TIME=(4,),
        D_VEHICLE_POSITION_IMG=(4, 60,),
        D_VEHICLE_SPEED_IMG=(4, 60,),
        D_VEHICLE_WAITING_TIME_IMG=(4, 60,),
    ),

    "LIST_STATE_FEATURE": [
        "cur_phase",
        "time_this_phase",
        "vehicle_position_img",
        "vehicle_speed_img",
        "vehicle_acceleration_img",
        "vehicle_waiting_time_img",
        "lane_num_vehicle",
        "lane_num_vehicle_been_stopped_thres01",
        "lane_num_vehicle_been_stopped_thres1",
        "lane_queue_length",
        "lane_num_vehicle_left",
        "lane_sum_duration_vehicle_left",
        "lane_sum_waiting_time",
        "terminal"
    ],

    "DIC_REWARD_INFO": {
        "flickering": 0,
        "sum_lane_queue_length": 0,
        "sum_lane_wait_time": 0,
        "sum_lane_num_vehicle_left": 0,
        "sum_duration_vehicle_left": 0,
        "sum_num_vehicle_been_stopped_thres01": 0,
        "sum_num_vehicle_been_stopped_thres1": -0.25
    },

    "LANE_NUM": {
        "LEFT": 1,
        "RIGHT": 0,
        "STRAIGHT": 1
    },

    "PHASE": [
        'WT_ET',
        'NT_ST',
        'WL_EL',
        'NL_SL',
        # 'WL_WT',
        # 'EL_ET',
        # 'SL_ST',
        # 'NL_NT',
    ],

    "list_lane_order": ["WL", "WT", "EL", "ET", "NL", "NT", "SL", "ST"],

    "phase_expansion": {
        1: [0, 1, 0, 1, 0, 0, 0, 0],
        2: [0, 0, 0, 0, 0, 1, 0, 1],
        3: [1, 0, 1, 0, 0, 0, 0, 0],
        4: [0, 0, 0, 0, 1, 0, 1, 0],
        5: [1, 1, 0, 0, 0, 0, 0, 0],
        6: [0, 0, 1, 1, 0, 0, 0, 0],
        7: [0, 0, 0, 0, 0, 0, 1, 1],
        8: [0, 0, 0, 0, 1, 1, 0, 0]
    },

    "phase_expansion_4_lane": {
        1: [1, 1, 0, 0],
        2: [0, 0, 1, 1],
    },

    "VALID_THRESHOLD": 30,

    "LOG_DEGUB": False,

    "N_LEG": 4,

}

_LS = {"LEFT": 1,
       "RIGHT": 0,
       "STRAIGHT": 1
       }
_S = {
    "LEFT": 0,
    "RIGHT": 0,
    "STRAIGHT": 1
}

dic_two_phase_expansion = {
    1: [1, 1, 0, 0],
    2: [0, 0, 1, 1],
}

# dic_four_phase_expansion = {
#     1: [0, 1, 0, 1, 0, 0, 0, 0],
#     2: [0, 0, 0, 0, 0, 1, 0, 1],
#     3: [1, 0, 1, 0, 0, 0, 0, 0],
#     4: [0, 0, 0, 0, 1, 0, 1, 0],
#     5: [1, 1, 0, 0, 0, 0, 0, 0],
#     6: [0, 0, 1, 1, 0, 0, 0, 0],
#     7: [0, 0, 0, 0, 0, 0, 1, 1],
#     8: [0, 0, 0, 0, 1, 1, 0, 0]
# }

DIC_TRANSFERDQN_AGENT_CONF = {
    "LEARNING_RATE": 0.001,
    "LR_DECAY": 1,
    "MIN_LR": 0.0001,
    "SAMPLE_SIZE": 1000,
    "BATCH_SIZE": 20,
    "EPOCHS": 100,
    "UPDATE_Q_BAR_FREQ": 5,
    "UPDATE_Q_BAR_EVERY_C_ROUND": False,
    "GAMMA": 0.8,
    "MAX_MEMORY_LEN": 10000,
    "PATIENCE": 10,
    "D_DENSE": 20,
    "N_LAYER": 2,
    "EPSILON": 0.8,
    "EPSILON_DECAY": 0.95,
    "MIN_EPSILON": 0.2,
    "LOSS_FUNCTION": "mean_squared_error",
    "SEPARATE_MEMORY": False,
    "NORMAL_FACTOR": 20,
    "TRAFFIC_FILE": "cross.2phases_rou01_equal_450.xml",
    "EARLY_STOP_LOSS": "val_loss",
    "DROPOUT_RATE": 0,
    "MERGE": "multiply"
}

DIC_PATH = {
    "PATH_TO_MODEL": "model/default",
    "PATH_TO_WORK_DIRECTORY": "records/default",
    "PATH_TO_DATA": "data/template",
    "PATH_TO_PRETRAIN_MODEL": "model/default",
    "PATH_TO_PRETRAIN_WORK_DIRECTORY": "records/default",
    "PATH_TO_PRETRAIN_DATA": "data/template",
    "PATH_TO_AGGREGATE_SAMPLES": "records/initial",
    "PATH_TO_ERROR": "errors/default"
}

DIC_AGENTS = {
    "TransferDQN": TransferDQNAgent,
}

DIC_ENVS = {
    # "sumo": SumoEnv,
    "anon": AnonEnv
}
