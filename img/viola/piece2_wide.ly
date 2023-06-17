\version "2.24.1"
\language "english"
\score
{
    % OPEN_BRACKETS:
    \new Staff
    {
        c'4
        % AFTER:
        % SPANNER_STARTS:
        (
        d'8
        e'8
        fs'2
        % AFTER:
        % ARTICULATIONS:
        - \fermata
        % SPANNER_STOPS:
        )
    % CLOSE_BRACKETS:
    }
}
