#include <iostream>

namespace
{
    static auto constexpr
}

EvacSM::EvacSM
{
    addTransitions();
    addActivities();
    printDotFile();
}

void EvacSM::addTransitions()
{
    // From, To, Trigger, Guard, Action, External
    _fsm.addTransitions({

      // Initial
      {
          State::Initial,
          State::DoorsReleased,
          DcoEvent::NoTrigger,
          FSM_GUARD([&](){ return leftDoorReleased() || rightDoorReleased(); }),
          FSM_NO_ACTION,
          TransitionType::External
      },
      {
          State::Initial,
          State::DoorsNotReleased,
          DcoEvent::NoTrigger,
          FSM_GUARD([&](){ return !leftDoorReleased() && !rightDoorReleased(); }),
          FSM_NO_ACTION,
          TransitionType::External
      },
      {
          State::DoorsReleased,
          State::DoorsReleased,
          DcoEvent::OnDoorReleaseMessage,
          // updateGuiWithDoorRelease should not be done here as we are trying to piggy back on the guard.
          // This would be changed once we separate mqtt event handling logic from the guard and action logic
          FSM_GUARD([&](){ handleDoorRelease(); return !leftDoorReleased() && !rightDoorReleased(); }),
          FSM_ACTION([&](){ exitEvacuationMode(); }),
          TransitionType::Internal
      },
      {
          State::DoorsNotReleased,
          State::DoorsNotReleased,
          DcoEvent::OnDoorReleaseMessage,
          FSM_GUARD([&](){ handleDoorRelease(); return !leftDoorReleased() && !rightDoorReleased(); }),
          FSM_ACTION([&](){ exitEvacuationMode(); }),
          TransitionType::Internal
      }
    });
}

void EvacSM::addActivities()
{
    _fsm.addActivities({
      {
      }
    });
}

