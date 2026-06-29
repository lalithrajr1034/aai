from langflow.custom import Component
from langflow.io import MessageTextInput, Output
from langflow.schema import Data


class HackathonStatusTracker(Component):
    display_name = "Hackathon Status Tracker"
    description = "Formats a hackathon task update into a clean status summary."
    icon = "file-text"
    name = "HackathonStatusTracker"
    inputs = [
        MessageTextInput(
            name="task_update",
            display_name="Task Update",
            info="Use format: Task | Worker | Status | Notes",
            tool_mode=True,
        ),
    ]
    outputs = [
        Output(
            display_name="Status Log",
            name="status_log",
            method="track_status",
        ),
    ]

    def track_status(self) -> Data:
        try:
            parts = [
                part.strip()
                for part in self.task_update.split("|")
            ]
            if len(parts) != 4:
                return Data(data = {"error": "Use format: Task | Worker | Status | Notes"})
            task, worker, status, notes = parts
            
            result = {
                "task": task,
                "worker": worker,
                "status": status,
                "notes": notes,
                "summary": f"Task: {task} | Worker: {worker} | Status: {status} | Notes: {notes}",
            }
            return Data(data=result)
        
        except Exception as e:
            return Data(data={"error": str(e)})
