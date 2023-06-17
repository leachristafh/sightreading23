\version "2.24.1"
\language "english"
\score
{
    % OPEN_BRACKETS:
    \context Score = "Score"
    \with
    {
        proportionalNotationDuration = #(ly:make-moment 1 8)
    }
    <<
        % OPEN_BRACKETS:
        \context Staff = "Staff_1"
        {
            % OPEN_BRACKETS:
            \context Voice = "Voice_1"
            {
                c'4
                d'4
                e'4
                f'4
                g'2
                g'2
                a'4
                a'4
                a'4
                a'4
                g'1
                a'4
                a'4
                a'4
                a'4
                g'1
            % CLOSE_BRACKETS:
            }
        % CLOSE_BRACKETS:
        }
    % CLOSE_BRACKETS:
    >>
}
