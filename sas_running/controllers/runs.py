from sqlmodel import select

from sas_running.models.runs import Run, RunCreate, RunUpdate


class RunController:
    def __init__(self, session):
        self.session = session

    def get_runs(self) -> list[Run]:
        return self.session.exec(select(Run)).all()

    def get_run_by_id(self, run_id: int) -> Run:
        return self.session.exec(select(Run).where(Run.id == run_id)).one()

    def create_run(self, run_create: RunCreate) -> Run:
        new_run = Run(
            distance=run_create.distance, time=run_create.time, date=run_create.date
        )
        self.session.add(new_run)
        self.session.commit()
        self.session.refresh(new_run)
        return new_run

    def delete_run(self, run_id: int) -> None:
        run = self.session.exec(select(Run).where(Run.id == run_id)).one()
        self.session.delete(run)
        self.session.commit()

    def update_run(self, run_id: int, run_update: RunUpdate) -> Run:
        run = self.session.exec(select(Run).where(Run.id == run_id)).one()
        if run_update.distance:
            run.distance = run_update.distance
        if run_update.time:
            run.time = run_update.time
        if run_update.date:
            run.date = run_update.date
        self.session.add(run)
        self.session.commit()
        self.session.refresh(run)
        return run
