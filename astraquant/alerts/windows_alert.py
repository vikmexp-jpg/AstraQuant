from win11toast import toast


class WindowsAlert:

    @staticmethod
    def send(alert):

        opportunity = alert.opportunity

        duration = (
            opportunity.last_updated
            - opportunity.started_at
        ).total_seconds() / 60

        toast(
            title=f"{alert.symbol} | {opportunity.state.value}",
            body=(
                f"ID      : {opportunity.id}\n"
                f"Option  : {opportunity.option}\n"
                f"Current : {opportunity.current_discount:.2f}  "
                f"Peak    : {opportunity.max_discount:.2f}\n"
                f"Updated : {opportunity.last_updated.strftime('%H:%M:%S')}"
            ),
        )