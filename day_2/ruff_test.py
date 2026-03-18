import animals
import ruff

#region agent log
import json, time, uuid
_DEBUG_LOG_PATH = "/home/felix/python_course/.cursor/debug-79af41.log"
def _log(hypothesisId: str, message: str, data: dict):
    with open(_DEBUG_LOG_PATH, "a", encoding="utf-8") as f:
        f.write(
            json.dumps(
                {
                    "sessionId": "79af41",
                    "id": f"log_{int(time.time()*1000)}_{uuid.uuid4().hex[:8]}",
                    "timestamp": int(time.time() * 1000),
                    "location": "exercise_solutions/day_2/ruff_test.py:4",
                    "message": message,
                    "data": data,
                    "runId": "pre-fix",
                    "hypothesisId": hypothesisId,
                }
            )
            + "\n"
        )
_log("H1", "script_start", {"note": "ruff_test.py executed"})
_log("H2", "ruff_imported", {"ruff_module": getattr(ruff, "__name__", None), "ruff_file": getattr(ruff, "__file__", None)})
_log("H3", "no_ruff_cli_invocation", {"note": "Importing ruff does not run the linter; CLI not called by this script"})
#endregion

m = animals.Mammals()
m.printMembers()

dangerous_fish = animals.dangerous.Fish()
dangerous_fish.printMembers()

harmless_birds = animals.harmless.Birds()
harmless_birds.printMembers()